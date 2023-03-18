import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode



def main():

    def load_file():
        """Load text from file"""
        uploaded_file = st.file_uploader("Upload Files",type=['txt'])

        if uploaded_file is not None:
            if uploaded_file.type == "text/plain":
                raw_text = str(uploaded_file.read(),"utf-8")
            return raw_text

    #load excel to streamlit
    def load_excel():
        """Load text from file"""
        uploaded_file = st.file_uploader("Upload Files",type=['xlsx'])

        if uploaded_file is not None:
            df = pd.read_excel(uploaded_file)
        return df

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


if __name__ == "__main__":

    # App title and description
    st.title("Задружение файлов")
    st.write("Загрузите файлы")
    # Load file
    # raw_text = load_excel()

