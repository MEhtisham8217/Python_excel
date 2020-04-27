import pandas as pd
data = pd.read_excel("Marriage.xlsx",sheet_name="data")

print(data["data"].sum())

q1=data[["year","data"]]
q1=q1.groupby("year").sum()
q1=q1.sort_values("data",ascending="True")
print(q1)
