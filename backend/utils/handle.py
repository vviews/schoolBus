import pandas as pd
import json

custom_header = ['index','student_id','firstname','lastname','nickname','level','month','price','debt','paid_amount','tt','description']

def read_excel_to_dict(file_name, sheet_name):
    df = pd.read_excel(file_name, sheet_name, skiprows=range(0,3), header=None, names=custom_header)
    data = []
    for index, row in df.iterrows():
        if row.isnull().all():
            break
        else:
            data.append(row)
    
    result_df = pd.DataFrame(data)
    json_data = result_df.to_json(index=False, force_ascii=False, orient='records')
    # print(json_data)
    return json_data , sheet_name
    
def read_excel_file(file_name):
    excel_file = pd.ExcelFile(file_name)
    print(excel_file.sheet_names)
    for sheet_name in excel_file.sheet_names:
        read_excel_to_dict(file_name,sheet_name)

        
# read_excel_file('../../data/08.xlsx')