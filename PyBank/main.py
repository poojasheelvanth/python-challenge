import os
import csv
import statistics

csvpath = os.path.join("..","Resources","budget_data.csv")


with open(csvpath, newline='', encoding= 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    Month =[]
    Total=[]
    Profit=[]
    for row in csvreader:
        Month.append(row[0])
        Total.append(int(row[1]))
    
    for n in range(len(Total)-1):
        if (n-1) < (len(Total)-1):
            diff=Total[n+1]-Total[n]
            Profit.append(diff)
        else:
            diff=0
            Profit.append(diff)
            
    Greatest_Increase_Month=(Month[(Profit.index(max(Profit))+1)]) 
    Greatest_Decrease_Month=(Month[(Profit.index(min(Profit))+1)]) 
    Average_Change=round(statistics.mean(Profit),2)
    Total_Months=len(Month)
    Total_Amount=sum(Total)

    def Results():
        return ("Financial Analysis\n"+
        "----------------------------\n"+
        f"Total Months: {Total_Months} \n"+
        f"Total: ${Total_Amount}\n"+
        f"Average  Change: ${Average_Change}\n"+
        f"Greatest Increase in Profits: {Greatest_Increase_Month} (${max(Profit)})\n"+
        f"Greatest Decrease in Profits: {Greatest_Decrease_Month} (${min(Profit)})\n") 
     
    print(Results())
    
"""
EXPORT OUTPUT TO TEXT FILE
"""
output_path = os.path.join("..", "Resources", "PyBankOutput.txt")

with open(output_path, 'w', newline='') as text:
    text.write(Results())
   
    