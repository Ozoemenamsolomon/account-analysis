
    # "- [X] import excel data\n",
    # "- [ ] get monthly sum of expenses\n",
    # "- [ ] get monthly sum of income\n",
    # "- [ ] get monthly average of expenses\n",
    # "- [ ] get top two categories of each month\n",
    # "- [ ] get top five entries of each month"
   
# import numpy as np  
from datetime import datetime
import pandas as pd

data=pd.read_excel("data/data.xlsx")

data.rename(str.lower, axis='columns', inplace=True)

# replace pending date with dummy date
dummy_date=datetime(2022,4,20,0,0,0)
data["date"]=data["date"].replace("Pending",dummy_date,inplace=True)

# divide the data into two parts:
# 1. expenses
# 2. income

expenses_data = data[data['counterparty']!="PAYMENT"]
payment_data = data[data['counterparty']=="PAYMENT"]

# group the data by month
expenses_data_grouped = expenses_data.groupby(pd.Grouper(key='date', freq='M')).sum()

# expenses_data_grouped_by_month = expenses_data.groupby(data.date.dt.month).sum()

# print(expenses_data_grouped_by_month)

# pd.to_datetime(expenses_data_grouped_by_month["date"]).month_name()
# expenses_data_grouped_by_month["date"]

# print(needed_cols.groupby(["category"]).sum())
print(expenses_data_grouped)