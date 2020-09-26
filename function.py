fat_cost = 5
prot_cost = 10
carb_cost = 8


def calculator(first, second, op):
    result = 0
    if op == 1:
        result = first + second
    elif op == 2:
        result = first - second
    elif op == 3:
        result = first / second
    elif op == 4:
        result = first * second

    return result


def am_i_healthy(carb, fat, protein):
    x = carb <= 30 and protein <= 60 and fat <= 10
    return x


def percentages(carb_gms, fat_gms, protein_gms):
    total = carb_gms + fat_gms + protein_gms
    return carb_gms * 100 / total, fat_gms * 100 / total, protein_gms * 100 / total


def cost_calc(c_gm, f_gm, p_gm):
    global fat_cost
    global prot_cost
    global carb_cost

    total_cost = carb_cost * c_gm + fat_cost * f_gm + prot_cost * p_gm

    return total_cost


def bmi_calc(height, weight):
    x = weight / ((height / 100) ** 2)

    if x >= 40:
        a = ("your bmi is " + str(x) + " you are morbidly obese")
    elif x <= 18.5:
        a = ("your bmi is " + str(x) + " you are undernourished")
    elif 18.5 < x < 24.9:
        a = ("your bmi is " + str(x) + "you are healthy")
    elif 30 < x < 39.9:
        a = ("your bmi is " + str(x) + "you are fat")
    elif 24.9 < x < 29.9:
        a = ("your bmi is " + str(x) + "you are overweight")
    else:
        a = "you have given wrong values for height and weight"

    return a


# function to output the largest of three numbers

def largest_num(x, y, z):
    # when x is the largest number
    if z < x > y:
        a = x
    # when y is the largest number
    elif x < y > z:
        a = y
    elif x < z > y:
        a = z
    return a


def find_the_three_letter_word(x):

    split_variable = x.split(" ")
    #number_of_words = len(split_variable)

    count = 0
    for i in split_variable:
        if len(i) == 3:
            count = count + 1
    return count

def divide(x, y):
    answer = float(x/y )
    return answer


