travelers = open("travels.txt","r")
date_M = {}
dates = []
max = 0
coun_m = 0
coun_kms = 0
for i in travelers:
    if str(i.split()[0:2]) in dates:
        date_M[str(i.split()[0:2])] += 1
    else:
        date_M[str(i.split()[0:2])] = 1
        dates.append(str(i.split()[0:2]))

print(date_M)
for i in dates:
    if date_M[i] > max:
        max = date_M[i]
        mx_date = i

print(mx_date)

#____________________________
travelers = open("travels.txt","r")

for i in travelers:


    if i.split()[2] == "Липки":
        coun_m += int(i.split()[6])

    if " ".join(i.split()[0:2]) == "1 октября":
        coun_kms += int(i.split()[4])

print(coun_m)
print(coun_kms)

#____________________________
travelers = open("travels.txt","r")
to = []
to_dct = {}
for i in travelers:

    if i.split()[3] in to:
        to_dct[i.split()[3]][0] += int(i.split()[6])
        to_dct[i.split()[3]][1] += 1
    else:
        to_dct[i.split()[3]] = [int(i.split()[6]),1]
        to.append(i.split()[3])
max_m = 0
max_cou = 0
for i in to:
    if max_m < to_dct[i][0]:
        max_m = to_dct[i][0]
    if max_cou < to_dct[i][1]:
        max_cou = to_dct[i][1]
print(max_m)
print(max_cou)
travelers.close()