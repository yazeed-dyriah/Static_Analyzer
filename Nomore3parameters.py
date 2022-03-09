
# coding: utf-8

# In[ ]:

################## 3 parameters #################


def NoMoreThanThreeParameters(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        for line in lines :
            commaCount=line.count(",")
            if(line.startswith('def') and commaCount+1 > 3):
                print("line :")
                print (line)
                print("// more than 3 parameters error")
                print'\n'
                print "******************************************************"



