inputvalues = input()
names = inputvalues.split()
for i in range(len(names)):
	names[i] = str(names[i]) 
shortest = names[0]
longest = names[0]

for i in range(len(names)):
    if len(shortest) > len(names[i]):
        shortest = names[i]
    if len(shortest) == len(names[i]):
        if shortest > names[i]:
            shortest = names[i]
    if len(longest) < len(names[i]):
        longest = names[i]
    if len(longest) == len(names[i]):
        if longest > names[i]:
            longest = names[i]

print(shortest, longest)