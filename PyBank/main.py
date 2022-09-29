#import dependencies
from audioop import avg
import csv
import os

#initialize variables
month =0
total = 0
date_col = []
profit_col = []
monthly_change = []
#create path to csv file aand output path
path = os.path.join('Resources','budget_data.csv')
output_path = os.path.join('analysis','output.txt')
#open and read csv file
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
#remove header of file
    csvheader= next(csvreader)

#loop to go through file
    for line in csvreader:
        date_col.append(line[0])
        profit_col.append(int(line[1]))
#get total months of period
        month = month + 1
#get total amount over period
        total = int(line[1])+ total
#get average change over period
    for i in range(len(profit_col)-1):
        monthly_change.append(profit_col[i+1]- profit_col[i])
    avg_change = sum(monthly_change)/ len(monthly_change)
    avg_change= float("{:.2f}".format(avg_change))
#get greatest increase over period
    increase = max(monthly_change)
    month_of_increase = monthly_change.index(increase)+1
#get greatest decrease over period
    decrease = min(monthly_change)
    month_of_decrease= monthly_change.index(decrease)+1
#print Statements
    print("Financial Analysis")
    print('---------------------------------')
    print(f'Total Months: {month}')
    print(f'Total: ${total}')
    print(f'Average Change: ${avg_change} ')
    print(f'Greatest Increase in Profits:  {date_col[month_of_increase]} (${increase})')
    print(f'Greatest Decrease in Profits: {date_col[month_of_decrease]} (${decrease})')
        
#output to text file
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write('-----------------------\n')
    file.write('Total Months: ' + str(month)+ "\n")
    file.write('Total: ' + '$'+ str(total)+ "\n")
    file.write('Average Change: '+ '$'+str(avg_change)+"\n")
    file.write('Greatest Increase in Profits: '+ str(date_col[month_of_increase])+ '  '+ '$'+str(increase)+'\n')
    file.write('Greatest Decrease in Profits: '+ str(date_col[month_of_decrease])+ '  '+ '$'+str(decrease))
    
    

