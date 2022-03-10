


oftware Testing and Quality Assurance
Static analyzer
 Report
 
 1_do_the_attribute
In this part there are two parts
The first section checked if it was on the order of the attribute
At first, I opened the file and accessed it
   with open(fileName) as file:
        lines = file.readlines()
        for line in lines:

For examination, the first thing must be access and distinction, that it is a function
  if line.startswith("def"):
Then to check attribute Distinguish and take between the brackets in the function in a variable arguments 
arguments = line[line.index('(') + 1:line.index(')')]



There is inside every function between the attribute breaks  ‘,’  used  spilt
arguments = arguments.split(',')
And then check if it int string string .
                arguments = arguments.split(',')
                if 'int' in arguments[0] \
                        and 'str' in arguments[1] \
                        and 'str' in arguments[2]:


The second part is to check the values of the attribute
The way to check if it ends in ‘)’
if line.endswith(')'):

Check the line if it starts with ‘) ‘and ends with’ (‘
Then check the numeric value (int) isdecimal 
and the second  value string '"'
And the third value string '"'

 sub_line = line[line.index('(') + 1:line.index(')')].split(',')

            if sub_line[0].isdecimal() and '"' in sub_line[1] and "'" in arguments[2]:
                Pass

If it is incorrect, then give a message incorrect value in call function"  and line 

![275398306_962554724626586_7285608609163383047_n](https://user-images.githubusercontent.com/78642805/157745902-c1827d74-5674-46f0-b324-f6a63750b51a.png)

2_Unreachable code after return statement : read the lines in the text file which is below (return) and give an error message , and if the line after return is (for,if,},{,) it will not give an error message on it.

3_ No more than 3 paramers:

I read the code in the txt file I wrote a python code to count the number of (',') in the line and check if line is functiona , by check if it is start with (def) ,then I check if it is a function and the value of the comma counter is more than 3 it will get an error message.

4_Devide By zero : I read the txt file line by line then and get the first character on the substring after ('/') ,and check if it digit or not , and if it is a digit , check if it 0 give error message.
6_magic number :

first, i read number from eof txt file I wrote a Python code to test the user entered code from file if the code include these cases its a magic number:

If the variable is preceded by ==, then it is a magic number.
If it is in the code Fail, Pass, Unknown then it is Magic Streng.
If the code has a comparison operation such as: >, <, >=, <= then it is magic number.
If it precedes it = then it is not your magic number.
