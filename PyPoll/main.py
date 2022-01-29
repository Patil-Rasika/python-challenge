import os
import csv


# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
# Open the CSV
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    votingdata=[]
    uniquenames = []
    # Loop through CSV
    for row in csvreader:
        if row[2] not in uniquenames :
            uniquenames.append(row[2])
        l1 = [row[0],row[1],row[2]] 
        votingdata.append(l1)

    #print(uniquenames) 

    votedic = dict()
    length = len(uniquenames)
    lengthdata = len(votingdata)
    total = lengthdata
    #print(lengthdata)
    #print(votingdata[0][2])
    #print("uniquenames" + str(length))


    for i in range(length):
       
        count = 0 
        for l in range(lengthdata):
            if votingdata[l][2] == uniquenames[i] :
               # print(uniquenames[i])
                count = count + 1 
        canditate = uniquenames[i]

        #print(uniquenames[i])
        #print(count)
        votedic.update({canditate : count})
    #print(votedic)


output_path = os.path.join( "Analysis", "votingoutput.txt")
with open(output_path ,'w') as f :
    f.write("Election Results")
    f.write('\n')
    f.write("-------------------------")
    f.write('\n')
    f.write("Total Votes: " + str(total))
    f.write('\n')
    f.write("-------------------------")
    f.write('\n')

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total))
    print("-------------------------")
    maxvote = 0
    winner = "" 
    for k, v in votedic.items():
        percent = round((v/total) * 100,4)
        print(k + " " + str(percent) + "%  (" + str(v) + ")"  )
        f.write(k + " " + str(percent) + "%  (" + str(v) + ")"  )
        f.write('\n')
        if v > maxvote :
           maxvote = v 
           winner = k 
    print("-------------------------")
    print ("Winner :" + winner)
    print("-------------------------")

    f.write("-------------------------")
    f.write('\n')
    f.write ("Winner :" + winner)
    f.write('\n')
    f.write("-------------------------")