import pandas as pd
file = pd.ExcelFile('ksuz retail system.xlsx')
file.sheet_names
df1 = file.parse('Clients')
df2 = file.parse('Products')
df3 = file.parse('Invoice')