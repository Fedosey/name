peper = open('Perepis.txt',"r")
count = 0
for i in peper:
    print(i.split(" ")[0])
    count +=1
    print(i)
    if int(i.split(" ")[6].split(".")[2])< 1978:
       print(i)
#----------------------------------------
print()
age_from = int(input())
age_two = int(input())
for i in peper:
   if age_from<int(i.split(" ")[6].split(".")[2])<age_two:
       name = i.split(" ")
       print(name[0],name[1],name[2],int(i.split(" ")[6].split(".")[2]))

peper.close()