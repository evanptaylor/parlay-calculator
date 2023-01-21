wager = float(input("Enter wager amount: "))
numTeams = int(input("Enter the number of teams in the parlay: "))
oddsList = []
total = 1

for i in range (0,numTeams):
    oddsList.append(input("Enter odds (+-) for team " + str(i+1) + ": "))

length = len(oddsList)
for i in range (0,length):
    if oddsList[i][0] == "+":
        oddsList[i] = oddsList[i][1:len(oddsList[i])]
        oddsList[i] = ((int(oddsList[i]))+100)/100
    else:
        oddsList[i] = oddsList[i][1:len(oddsList[i])]
        oddsList[i] = ((int(oddsList[i]))+100)/int(oddsList[i])

for i in range (0,length):
    total = total*oddsList[i]

total = total - 1
print("")
print(str(len(oddsList)) + " Team Parlay:")
if total >= 1:
    print("+"+str(round(total*100)))
else:
    print("-"+str(round(100/total)))
print("A " + str(wager) + " bet earns " + str(round((total*wager))))
        
