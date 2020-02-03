

stringA = 'Norwegian Blue'
count = 0
print(stringA)

for i in range(len(stringA)):
    if (stringA[i] == "w" or (stringA[i] == "e" and count == 1) or stringA[i] == " "): 
        print(stringA[i])
        count = count + 1

for i in range(len(stringA)):
    if (stringA[i] == "w" or (stringA[i] == "i") or stringA[i] == "n"): 
        print(stringA[i])

    
print()

print(stringA[3])
print(stringA[4])
print(stringA[9])
print(stringA[3])
print(stringA[6])
print(stringA[8])

print()

print(stringA[-11])
print(stringA[-10])
print(stringA[-5])
print(stringA[-11])
print(stringA[-8])
print(stringA[-6])
my = 1

print()

my = 2

print(stringA[3 - len(stringA)])
print(stringA[4 - len(stringA)])
print(stringA[9 - len(stringA)])
print(stringA[3 - len(stringA)])
print(stringA[6 - len(stringA)])
print(stringA[8 - len(stringA)])


stringA = 'Norwegian Blue'
print(stringA[10:10])