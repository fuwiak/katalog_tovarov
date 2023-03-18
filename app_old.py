import pandas as pd
import streamlit as st
import numpy as np

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

def show_table_grid(data):
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()
    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=True,
        enable_enterprise_modules=True,
        height=600,
        width='100%',
        reload_data=True
    )
    return grid_response

path ='data/data.xlsx'
df = pd.read_excel(path, skiprows=1) #чтение данных



#markdown
st.markdown(''' ### Вытащенные товары ''')

#load excel to streamlit in sidebar

excel_file = st.sidebar.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
if excel_file is not None:
    df = pd.read_excel(excel_file, skiprows=1)

    show_table_grid(df)


#select box unique values
st.markdown(''' ### Выберите товар ''')

select = st.selectbox('Выберите товар', df['Наименование товара'].unique())
st.markdown(''' ### Выбранный товар ''')
if select is not None:
    temp = df[df['Наименование товара'] == select]
    #show all unique values
    st.write(temp)
    indexes = temp.index.values
    diffs = np.diff(indexes)

st.markdown(''' ### Выберите КТРУ/ОКПД2 ''')

select = st.selectbox('Выберите КТРУ/ОКПД2', df['КТРУ/ОКПД2'].unique())
st.markdown(''' ### Выбранный КТРУ/ОКПД2 ''')
if select is not None:
    temp = df[df['КТРУ/ОКПД2'] == select]
    st.write(temp)
    indexes = temp.index.values
    diffs = np.diff(indexes)
    indices = [(indexes[i],indexes[i+1]) for i in range(len(indexes)-1) if diffs[i] > 1]
    if len(indices) > 0:
        indices.append((indexes[-1], indexes[-1]+diffs[-1]))
    else:
        indices.append((indexes[0], indexes[0]+12))

    #select columns
    st.markdown(''' ### Выберите колонки ''')
    select = st.multiselect('Выберите колонки', df.columns,
                            default=['Наименование показателя'])

    st.markdown(''' ### Выбранные колонки ''')
    if select is not None:
        temp = df[select]
        #show all unique values
        unique_values = temp['Наименование показателя'].unique()
        st.write(unique_values)
        #select values
        st.markdown(''' ### Выберите значения ''')
        select = st.multiselect('Выберите значения', unique_values,
                                default=[unique_values[0]])
        st.markdown(''' ### Выбранные значения ''')
        if select is not None:
            temp = df[df['Наименование показателя'].isin(select)]
            #select columns
            st.markdown(''' ### Выберите колонки ''')
            select = st.multiselect('Выберите колонки', temp.columns,
                                    default=temp.columns[0])

            st.write(temp[select])



