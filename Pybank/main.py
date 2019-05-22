import pandas as pd
import numpy as np
import csv
import os

budget_data=pd.read_csv("dataset/budget_data.csv")
output = os.path.join("summary/budget_summary.txt")

total_months=len(budget_data["Date"]) 
net_total=budget_data["Profit/Losses"].sum()
budget_data["average_difference"]=budget_data["Profit/Losses"].diff()
average_change=round(budget_data["average_difference"].mean(),2)

max_profit=budget_data["average_difference"].max()
max_date=(budget_data.Date[budget_data.average_difference==max_profit]).values[0]
min_profit=budget_data["average_difference"].min()
min_date=(budget_data.Date[budget_data.average_difference==min_profit]).values[0]

poll_results_summary=("Financial Analysis\n"
"------------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${net_total}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {max_date} (${max_profit})\n"
f"Greatest Increase in Profits: {min_date} (${min_profit})\n")

print(poll_results_summary)
with open(output, "w") as txt_file:
    txt_file.write(poll_results_summary)
