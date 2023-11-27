import pandas as pd


def read_file(file_path):
    df = pd.read_excel(file_path)
    selected_columns = df.loc[:, ['event', '是否含有r_info', ]]
    return selected_columns

