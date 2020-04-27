import pandas as pd
data = pd.read_excel("Marriage.xlsx",sheet_name="data")

q2=data[(data["Emirate_EN"]==' Abu Dhabi') |(data["Emirate_EN"]==' Dubai') | (data["Emirate_EN"]==' Sharjah') ]

q2=q2.groupby(["Emirate_EN","year"]).sum()
print(q2)
