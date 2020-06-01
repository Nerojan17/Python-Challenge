import csv
import os


csv_path = os.path.join("Resources", "budget_data.csv")

month = []
profit = []


with open (csv_path, "r", newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")

    headers = next(csv_reader)


    for line in csv_reader:
        month.append (line[0])
        profit.append (float(line[1]))

num_months = len(month)

m_over_m_change = []

for i in range(1, num_months):
    m_over_m_change.append (profit[i]- profit[i-1])


total_profit = sum(profit)

averge_chg_profit = sum(m_over_m_change)/len(m_over_m_change)

max_change = max(m_over_m_change)

max_change_month = month[m_over_m_change.index(max_change)+1]

min_change = min(m_over_m_change)   

min_change_month = month[m_over_m_change.index(min_change)+1]

print(total_profit)
print(averge_chg_profit)
print(max_change)
print(min_change)
print(max_change_month)
print (min_change_month)
print(headers)


output_path = os.path.join("Analysis", "results.txt")

with open (output_path, "w", newline= "") as csv_output_file:
    csv_writer = csv.writer (csv_output_file, delimiter= ",")

    csv_writer.writerow(["Financial Analysis"])
    csv_writer.writerow(["Total Months: " + str(num_months)])
    csv_writer.writerow(["Total Profit: " + str(total_profit)])
    csv_writer.writerow(["Average change: " + str(averge_chg_profit)])
    csv_writer.writerow(["Greatest Increase: " + str(max_change_month) + " " + str(max_change)])
    csv_writer.writerow(["Greatest Decrease: " + str(min_change_month) + " " + str(min_change)])