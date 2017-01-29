def greeting(name,age):
    """ Mohammed Salman
        Metropolia university of Applied Sciences
        Assignment 3: Functions
        28.01.2017"""
    favorite_colour = input("What is your favorite colour?  ")
    strings = (name, age, favorite_colour)
    import time
    temp = (age - int(time.strftime("%d")))
    temp2 = int(time.strftime("%H"))
    lucky_number= (temp % temp2)
    output = "Hi, my name is {0}, I am {1} years old, amd I like {2} \n Today is {3}. \n My lucky number is {4}".format(strings[0], strings[1], strings[2], time.strftime("%d.%m.%Y"), lucky_number)
    return output
print(greeting('Muhis',26))
print(greeting.__doc__)
