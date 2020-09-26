def calculator(first, second, op):
    if op == 1:
        result = first + second
    elif op == 2:
        result = first - second
    elif op == 3:
        result = first / second
    else:
        result = first * second

    return result


# print("enter the first number of your calculation")
# a = int(input())
# b = int(input("enter the second number"))
# print("Choose your operation")
# print("1)Add")
# print("2)Subtract")
# print("3)Divide")
# print("4)Multiply")
# op= int(input("enter the number 1 or 2 or 3 or 4" ))
# output=calculator(a, b, op)
# print (output)