import pandas as pd
import os

# def get_login_data():
#     file_path = os.path.join(
#         os.path.dirname(os.path.dirname(__file__)),
#         "test_data",
#         "testdata.xlsx"
#     )
#     data = pd.read_excel(file_path)
#     print(data.values.tolist())   # 👈 DEBUG (see what Excel gives)
#     return data.values.tolist()

def get_excel_data(sheet_name):
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "test_data",
        "testdata.xlsx"
    )
    data = pd.read_excel(file_path,sheet_name=sheet_name)
    print(data.values.tolist())   # 👈 DEBUG (see what Excel gives)
    return data.values.tolist()



