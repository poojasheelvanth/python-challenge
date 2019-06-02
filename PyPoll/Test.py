import os
import csv
import statistics

csvpath = os.path.join("..","Resources","Jump.csv")


with open(csvpath, newline='', encoding= 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        operand = row[1]
        if operand == "+":
            answer =row[0]+row[2]
        else if operand == "*":
            answer =row[0]*row[2]
        print(answer)