
# coding: utf-8

# In[1]:

####################### unreachable code ###############

def UnreachableCode(fileName):
    with open(fileName, 'r') as File:
        while not 'return' in next(File):
            pass
        for line in File:
            if "else" not in line and "for" not in line and "if" not in line and '}' not in line and '{' not in line and '\n' not in line :
                print("line :")
                print(line)
                print("// These unreachable code")
                print'\n'
                print "******************************************************"


