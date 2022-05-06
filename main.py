import calendar
from cmath import exp
import datetime
import pandas as pd


# - [X] import excel data
# - [X] get monthly sum of expenses
# - [ ] get monthly sum of income
# - [ ] get monthly average of expenses
# - [ ] get top two categories of each month
# - [ ] get top five entries of each month



raw_data = pd.read_excel("data/data.xlsx")

raw_data['Date']=raw_data['Date'].replace("Pending",pd.Timestamp.now())
date=raw_data['Date']
raw_data["Month_Value"] = pd.DatetimeIndex(raw_data['Date']).month
raw_data["Month"] = raw_data['Date'].dt.month_name()


income_data=raw_data[raw_data["Counterparty"]=="PAYMENT"]
expenses_data=raw_data[raw_data["Counterparty"]!="PAYMENT"]


expenses_grouped_by_month=expenses_data.groupby(["Month_Value","Month"]).sum()

# expenses_grouped_by_month["Month"]=raw_data["Month"].apply(lambda x:calendar.month_name[x])

# print(raw_data['Month'].describe())

print(expenses_grouped_by_month.droplevel("Month_Value"))