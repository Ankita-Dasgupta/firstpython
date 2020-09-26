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


