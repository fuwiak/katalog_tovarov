import pandas as pd
import numpy as np
import streamlit as st
import mpld3
import streamlit.components.v1 as components
import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd
import streamlit as st
import numpy as np
from typing import List, Dict, Any, Union, Optional
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
from streamlit_searchbox import st_searchbox
from streamlit_extras.word_importances import format_word_importances


st.title("Визуализация данных")

df = pd.read_excel('data/data.xlsx')

excel_file = st.sidebar.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
if excel_file is not None:
    df = pd.read_excel(excel_file, skiprows=1)

input = st.text_area("Впишите описание продукта :")

def show_importances(text: str) -> str:

    words = text.split()
    # importances_list the same as words length
    importances_list = np.random.rand(len(words))
    html = format_word_importances(words, importances_list)
    return html

html = show_importances(input)

st.write(html, unsafe_allow_html=True)




# text = (
#     input
# )
#
#
#
#
#
#
# html = format_word_importances(
#     words=text.split(),
#     importances=(0.1,0.1),  # fmt: skip
# )
# st.write(html, unsafe_allow_html=True)
#
# c1, c2, c3 = st.columns(3)
#
# def search_sth_fast(searchterm: str) -> List[str]:
#     """
#     function with list of strings
#     """
#     return [f"{searchterm}_{i}" for i in range(10)]
#
# with c1:
#
#     selected_value2 = st_searchbox(
#         search_sth_fast,
#         default=None,
#         label="search_sth_fast",
#         clear_on_submit=True,
#         key="search_sth_fast",
#     )
#     st.info(f"{selected_value2}")
#
# # input = st.text_area("Enter Input Data :")
#
# output = input.upper() # final_result_from_processing_the_input
#
# st.text_area(label="Output Data:", value=output, height=350)
