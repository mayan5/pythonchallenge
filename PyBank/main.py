import os
import csv
csvpath = "Resources_budget_data.csv"
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_months = 0
    total_revenue = []
    monthly_profit_change = []

    profit_loss_list = []

    month_list = []
    for row in csvreader:
        total_months = total_months + 1
        month_list.append(row[0])
        profit_loss_list.append(int(row[1]))
    print(total_months)
    print(month_list)
    

    #total_months = len(month_list)
    net_profit_loss = sum(profit_loss_list)

    
    print(net_profit_loss)

    average_monthly_change_list = []
    previous_month_amount = 0

    for x in range(len(profit_loss_list)):
        if x == 0:
            previous_month_amount = profit_loss_list[x]
        else:
            monthly_change = profit_loss_list[x] - previous_month_amount
            average_monthly_change_list.append(monthly_change)
            previous_month_amount = profit_loss_list[x]
    print(average_monthly_change_list)
    print(max(average_monthly_change_list))
    print(min(average_monthly_change_list))
    print(sum(average_monthly_change_list)/len(average_monthly_change_list))