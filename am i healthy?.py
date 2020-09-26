fat_cost = 5
prot_cost = 10
carb_cost = 8

def am_i_healthy (carb, fat, protein):
    x=carb<= 30 and protein<= 60 and fat <=10
    return x

def percentages (carb_gms, fat_gms, protein_gms):
    total= carb_gms + fat_gms + protein_gms
    return carb_gms * 100/total, fat_gms * 100/total, protein_gms*100/total

def cost_calc (c_gm, f_gm, p_gm):

    global fat_cost
    global prot_cost
    global carb_cost


    total_cost= carb_cost * c_gm + fat_cost * f_gm + prot_cost * p_gm

    return total_cost

carbs= int(input("enter your carb intake in grams"))
proteins= int(input("enter your protein intake in grams"))
fats= int(input("enter your fat intake in grams"))

car_P, fat_p, prot_p = percentages(carbs,fats,proteins)

print (am_i_healthy(car_P, fat_p, prot_p))

print (calculator.calculator(1,10,1 ))


print ("The total cost of your diet is ", cost_calc(carbs, fats, proteins))