import csv

path = 'Resources/budget_data.csv'
write_path = 'analysis/analysis.txt'
profit_loss, change, change_sum, prev, months, max_gain, max_loss = 0, 0, 0, 0, 0, 0, 0
gain_month, loss_month = '', ''

with open(path) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    next(csvreader)

    for row in csvreader:
        months += 1
        profit_loss += int(row[1])
        if prev == 0:
        	prev = int(row[1])
        change = int(row[1]) - prev
        change_sum += change
        if change > max_gain:
            max_gain = change
            gain_month = row[0]
        if change < max_loss:
            max_loss = change
            loss_month = row[0]
        prev = int(row[1])
output = f''' Financial Analysis
  ----------------------------
  Total Months: {months}
  Total: ${profit_loss}
  Average  Change: ${round(change_sum/months,2)}
  Greatest Increase in Profits: {gain_month} (${max_gain})
  Greatest Decrease in Profits: {loss_month} (${max_loss})'''
print(output)
with open(write_path, 'w') as file:
    file.write(output)

