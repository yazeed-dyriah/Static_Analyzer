

def do_the_attrbute(fileName):
    result = False
    with open(fileName) as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("def"):
                arguments = line[line.index('(') + 1:line.index(')')]

                arguments = arguments.split(',')
                if 'int' in arguments[0] \
                        and 'str' in arguments[1] \
                        and 'str' in arguments[2]:

                    result = True

    if result == False:
        print('incorrect arguments order')
        return

    for line in lines:

        if line.endswith(')'):

            sub_line = line[line.index('(') + 1:line.index(')')].split(',')

            if sub_line[0].isdecimal() and '"' in sub_line[1] and "'" in arguments[2]:
                pass
            else:
                print("incorrect value in call function", line)


def DivvideByZero(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        substring = '/'
        for line in lines:
            if line != None and substring in line:
                divisor = line.split('/', 1)[1]
                digit = (divisor[0].isdigit())
                if(digit == True):
                    if (int(divisor[0]) == 0):
                        print("line :")
                        print(line)
                        print("// Divide by zero error")


def MagicNumber(fileName):
    with open(fileName) as file:
        lines = file.readlines()
    for line in lines:
        if '==' in line and line.startswith("if") or line.startswith("else if"):
            argument = line[line.index('')]
            print("line:")
            print(line)
            print("is a magic number or string")
            print('\n')
            print("****************************************************")

        elif '<' in line or '>' in line or '<=' in line or '>=' in line or '*' in line or '-' in line or '+' in line or '/' in line and line.startswith("if") or line.startswith("else if"):
            print("line:")
            print(line)
            print("is a magic number because include an 'operation'")
            print('\n')
            print("****************************************************")


def NoMoreThanThreeParameters(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        for line in lines:
            commaCount = line.count(",")
            if(line.startswith('def') and commaCount+1 > 3):
                print("line :")
                print(line)
                print("// more than 3 parameters error")


def UnreachableCode(fileName):
    with open(fileName, 'r') as File:
        while not 'return' in next(File):
            pass
        for line in File:
            if(line != '\n'):
                if "else" not in line and "for" not in line and "if" not in line and '}' not in line and '{' not in line:
                    print("line :")
                    print(line)
                    print("// These unreachable code")


def main():
    print("______________________")
    do_the_attrbute("test.txt")
    DivvideByZero("test.txt")
    MagicNumber("test.txt")
    NoMoreThanThreeParameters("test.txt")
    UnreachableCode("test.txt")


if __name__ == '__main__':
    main()
