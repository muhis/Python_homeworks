def loop(variables):
    """        Author: Mohammed Salman
        Metropolia university of Applied Sciences
        Assignment 5: Loops
        29.01.2017"""
    for i in variables:
        if not(isinstance(i,(int,float,complex))):
            return 0
    i = 0
    summation = 0
    while (i < len(variables) and variables[i] != 0):
        summation += variables[i]
        i += 1
    return summation

print(loop([1,2,3,4,0,5]))
