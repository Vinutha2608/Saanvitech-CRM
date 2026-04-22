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

def get_add_new_client(sheet_name):
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "test_data",
        "testdata.xlsx"
    )

    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # 🔥 Filter row where Status = NO
    pending = df[df["Status"].str.upper() == "NO"]

    if pending.empty:
        return None

    return pending.iloc[0]   # take first NO row



