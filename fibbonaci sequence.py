print("welcome to fibonacci's sequence printer")
termination_number = int(input("enter the number of numbers in the sequence-> "))

n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if termination_number <= 0:
 print("Please enter a positive non zero integer-> ")
else:
 print("Fibonacci sequence:-")
 while count < termination_number:
  print(n1)
  nth = n1 + n2
  # update values
  n1 = n2
  n2 = nth
  count += 1