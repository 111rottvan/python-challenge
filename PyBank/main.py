import os
import csv
csvpath = os.path.join("budgetdata.csv")
mylist = []
TotalPnL = 0
initialval = 0
emptylist = []
greatest_up = ["", 0]
greatest_down = ["", 9999999]

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
#print(csvreader)
    next(csvreader)
    for row in csvreader:
        #print(row)
        mylist.append(row)
        #print(mylist)
    #print(len(mylist))
    for volume in mylist:
        #print(volume[1])
        TotalPnL = TotalPnL + int(volume[1])
        Changes=int(volume[1]) - initialval
        initialval = int(volume[1])
        emptylist.append(Changes)
        #print(initialval)
        #print(Changes)
    #print(TotalPnL)
    # list sllicing reorder the list 
    newIndex = emptylist[1:]
    AvgChange = sum(newIndex) /len(newIndex)  
    #print(AvgChange)
    #print(emptylist)
    #print(newIndex)
    #print(emptylist)
        if Changes> greatest_up[1]:
            greatest_up[1]=Changes
            greatest_up[0])=row["Date"]
        if Changes<greatest_up[1]):
            greatest_down[1]=Changes
            greatest_down[0]=row["Date"]
    print("Financial Analysis") 
    Print("--------------------------------------------------") 
    print("Total Months: ", len(mylist))  
    print("Total Revenue: ", TotalPnL)
    print("Average Revenue Change: ", AvgChange)
    print("Greatest Increase in Revenue: ", (greatest_up[0],greatest_up[1]))
    print("Greatest Decrease in Revenue: ", (greatest_down[0],greatest_down[1]))