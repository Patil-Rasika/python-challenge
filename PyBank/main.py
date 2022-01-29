# Modules
import os
import csv

TotalMonths =0 
Total = 0.0
avechange = 0 
MaxInProfit = 0 
MaxDecInProfit = 0 
MaxDate=""
MinDate = ""

proflosschange =[]
indexcounter = 0
prevpl = 0.0
nextpl =0.0

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #print(header)
    # Loop through CSV
    for row in csvreader:
        #print(row[0] + "  " + row[1] + "  ")
        TotalMonths = TotalMonths  + 1
        Profitloss = float(row[1])
        nextpl = Profitloss
        Total = Total + (Profitloss) 
        if Profitloss > MaxInProfit :
            MaxInProfit = Profitloss
            MaxDate = row[0] 
        if Profitloss < MaxDecInProfit :
            MaxDecInProfit = Profitloss
            MinDate = row[0]
        #print(nextpl)
        if  prevpl != 0.0 and nextpl !=0.0 :
           #print( "change" + str(nextpl - prevpl))
            proflosschange.append(nextpl - prevpl)
            indexcounter = indexcounter + 1
            #print("index" + str(indexcounter))
        prevpl = nextpl 
#print(str(len(proflosschange)))
total = 0.0
for number in proflosschange:
    total += number
average = round(total/len(proflosschange),2)

print("Financial Analysis") 
print("-----------------------------------------------------------")
print(" Total Months : " + str(TotalMonths )   )
print(" Total  : '$'" + str(Total )   )
print("Average  Change: '$'" + str(average))
print ("Greatest Increase in Profits: " +  MaxDate + " " +"''$"+ str(MaxInProfit))
print ("Greatest Decrease in Profits: " +  MinDate + " " +"'$'" +str(MaxDecInProfit))

FinAnalysis = {
    "Total Months :":  str(TotalMonths ) ,
    "Total :": str(Total ) ,
    "Average  Change: '$'": str(average),
    "Greatest Increase in Profits: ": str(MaxDate )+  " " +"''$"+ str(MaxInProfit),
    "Greatest Decrease in Profits: ": str(MinDate) + " " +"'$'" +str(MaxDecInProfit)
}
#print(FinAnalysis)

# save the output file path
output_file = os.path.join("Analysis","output.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    
    for k, v in FinAnalysis.items():
        value = k + v
        #print(value)
        writer.writerow( k  + v)

        

