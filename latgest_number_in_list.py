lst=[]
count=int(input('How many numbers?'))
for n in range(count):
    number = int(input('Enter number:'))
    lst.append(number)
print('Largest element of the list is:', max(lst))
