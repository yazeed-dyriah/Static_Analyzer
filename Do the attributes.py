

def do_the_attrbute():
    result = False
    with open('test.txt') as f:
        lines = f.readlines()
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


def main():
    print("______________________")
    do_the_attrbute()


if __name__ == '__main__':
    main()
