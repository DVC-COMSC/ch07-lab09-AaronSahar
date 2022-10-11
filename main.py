inputvalues = input()
names = inputvalues.split()
for i in range(len(names)):
	names[i] = str(names[i]) 
shortest = min(names, key=len)
longest = max(names, key=len)
print(shortest, longest)