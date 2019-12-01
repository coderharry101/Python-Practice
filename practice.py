#List
List = ['N','E','L','S','O','N']
print(List)

for name in List:
	print(List)

List.append("_")
List.append("M")
List.append("A")
List.append("N")
List.append("D")
List.append("E")
List.append("L")
List.append("A")
print(List)

print("".join(List))

del List[6:]
print(List)

# TABLE OF 2
for i in range(1,11):
	print(i*2)

#Dictionary
dict1 = {"Name": "Harry", "Age": 21, "Country": "India", "Hobbies": "Coding", "Education": "Soft.Engg."}
print(dict1)
for k,v in dict1.items():
	print(k, v)

for k, v in enumerate(['Tic', 'Tac', 'Toe']):
	print(k, v)

print(dict1['Country'])
