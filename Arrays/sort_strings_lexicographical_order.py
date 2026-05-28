strings = ["Amarnath","is","trying","to","study"]
for i in range(len(strings)):
    for j in range(0,len(strings)-i-1):
        if strings[j] > strings[j+1]:
            temp = strings[j]
            strings[j] = strings[j+1]
            strings[j+1] = temp
print(strings)