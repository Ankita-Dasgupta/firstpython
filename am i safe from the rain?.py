def am_i_safe (rain,hood,umb,workday):


    p=  rain_level <= 5 and hood or rain >5 and umb or not workday and rain >=15

    return p



rain_level= int(input("enter rain level in cms: "))
hood= input ("do you have on a hood? ")
workday=input ("is it a workday today? ")
umbrella=input ("do you have an umbrella? ")

p = rain_level <= 5 and hood or rain_level > 5 and umbrella or not workday and rain_level >= 15

#print (am_i_safe(rain_level,hood,umbrella,workday))

print (p)