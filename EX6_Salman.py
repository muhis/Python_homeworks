import re
def comments(from_file, to_file):
        """        Author: Mohammed Salman
            Metropolia university of Applied Sciences
            Assignment 6: Files
            29.01.2017"""
    if from_file[-3:] == '.py':
        pyfile = open(from_file).readlines()
        fwrite = open(to_file,'w')
    for i in range(len(pyfile)):
        if(re.search('#',pyfile[i])):
            fwrite.write(pyfile[i])
    return(true)
comments('EX4_Salman.py','output.txt')
