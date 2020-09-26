# Input name
print("type yes if you want shortform of your name and type no if you want your full name")
option_shortform = input()
number_of_elements = 0;
while (number_of_elements != 2):

    name = input("enter your full name")
    # split into firstname and lastname ( 2 variable)
    p = name.split()
    number_of_elements = len(p)
    if number_of_elements != 2:
        print('Enter first and lastname only')

if option_shortform[0].lower() == "n":
    firstName, lastName = p[0], p[1]
    # two more variable for first letter and rest for each firstname and lastname
    x = str(firstName[0].upper())
    y = str(firstName[1:].lower())
    a = str(lastName[0].upper())
    b = str(lastName[1:].lower())
    # add the variables and print
    print(x + y, a + b)

if option_shortform[0].lower() == "y":
    firstName, lastName = p[0], p[1]
    l1 = str(firstName[0].upper())
    l2 = str(lastName[0].upper())
    print(l1 + '.' + l2)
