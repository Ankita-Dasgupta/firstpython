import random
data = []
for j in range(100):
    data.append(random.randint(1, 200))
data.sort()


for i in range (1, 101):
    data.append(i)
search_term=int(input("Enter a number to search for in the list"))
low = 0
high = len(data) - 1
while low <= high:
    middle = (low + high) // 2

    if search_term not in (data):
        print("number is not in the list")
        break
    else:
        if data[middle] == search_term:
            print("position is", middle+1)
            break

        elif data[middle] > search_term:
            high = middle - 1
        else:
            low = middle + 1


