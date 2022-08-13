import pandas as pd

filepath = r'F:\OneDrive - 천안중앙고등학교\pythonworkspace\PROJECT\대학지도제작PRJ\고등교육기관 하반기 주소록(2021).xlsx'
excel_file = pd.read_excel(filepath,engine='openpyxl')
excel_file.columns = excel_file.loc[4].tolist()
excel_file = excel_file.drop(index=list(range(0,5)))

print(excel_file.head())
print(excel_file['학교명'].values)
print(excel_file['주소'].values)