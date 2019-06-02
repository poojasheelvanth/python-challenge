import os
import csv
import statistics

csvpath = os.path.join("..","Resources","election_data.csv")


with open(csvpath, newline='', encoding= 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    Voter =[]
    Khan=[]
    Correy=[]
    Li=[]
    Tooley=[]

    Winner =[len(Khan),len(Correy),len(Li),len(Tooley)]
    
    for row in csvreader:
        Voter.append(row[0])
        if row[2]=="Khan":
            Khan.append(row[0])
        elif row[2] == "Correy":
            Correy.append(row[0])
        elif row[2] == "Li":
            Li.append(row[0])
        elif row[2]=="O'Tooley":
            Tooley.append(row[0])
        
    Khan_percent=len(Khan)*100/len(Voter)
    Khan_percent_value = ("{0:.3f}".format(round(Khan_percent,3)))
    Total_Khan=len(Khan)   

    Correy_percent=len(Correy)*100/len(Voter)
    Correy_percent_value = ("{0:.3f}".format(round(Correy_percent,3)))
    Total_Correy=len(Correy)

    Li_percent=len(Li)*100/len(Voter)
    Li_percent_value = ("{0:.3f}".format(round(Li_percent,3)))
    Total_Li=len(Li)

    Tooley_percent=len(Tooley)*100/len(Voter)
    Tooley_percent_value = ("{0:.3f}".format(round(Tooley_percent,3)))
    Total_Tooley=len(Tooley)
    
    Total_Votes=len(Voter)
    Winner =[Total_Khan,Total_Correy,Total_Li,Total_Tooley]

    if max(Winner) == Winner[0]:
        Win= "Khan"
    elif max(Winner) == Winner[1]:
        Win= "Correy"
    elif max(Winner) == Winner[2]:
        Win= "Li"
    elif max(Winner) == Winner[3]:
        Win= "O'Tooley"
    

    def Results():
        return ("Election Results\n"+
        "----------------------------\n"+
        f"Total Votes: {Total_Votes}\n"+
        "----------------------------\n"+    
        f"Khan:  {Khan_percent_value}% ({Total_Khan})\n"+
        f"Correy: {Correy_percent_value}% ({Total_Correy})\n"+
        f"Li: {Li_percent_value}% ({Total_Li})\n"+
        f"O'Tooley: {Tooley_percent_value}% ({Total_Tooley}) \n"+
        "----------------------------\n"+ 
        f"Winner: {Win}\n"+
        "----------------------------\n") 
     
    print(Results())
    
"""
EXPORT OUTPUT TO TEXT FILE
"""
output_path = os.path.join("..", "Resources", "PyPollOutput.txt")

with open(output_path, 'w', newline='') as text:
    text.write(Results())
   
    