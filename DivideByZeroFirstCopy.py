
# coding: utf-8

# In[1]:

################# devide by zero when digit after / is 0  ###################


def DivvideByZero(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        substring = '/'
        for line in lines :
            if line != None and substring in line:
                divisor= line.split('/',1)[1]
                digit=(divisor[0].isdigit())
                if(digit==True):
                    if ( int(divisor[0])==0):
                        print("line :")
                        print(line)
                        print ("// Divide by zero error")
                        print '\n'
                        print "******************************************************"
 

    

