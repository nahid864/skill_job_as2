name = str(input('Enter any name: '))
letter = str(input("Enter a letter :"))
lst = []
for i in name:
    lst.append(i)
count=0
for i in lst:
    if i == letter:
        count = count+1
    else:
        continue
print(count)
