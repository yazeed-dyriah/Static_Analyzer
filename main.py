def MagicNumber(fileName):
    with open("eof.txt") as file:
        lines = file.readlines()
    for line in lines:
        if '==' in line and line.startswith("if") or line.startswith("else if"):
            argument = line[line.index('')]
            print("line:")
            print (line)
            print("is a magic number or string")
            print('\n')
            print ("******************************************************")

        elif '<' in line or '>' in line or '<=' in line or '>=' in line or '*' in line or '-' in line or '+' in line or '/' in line and line.startswith("if") or line.startswith("else if"):
            print("line:")
            print(line)
            print("is a magic number because include an 'operation'")
            print('\n')
            print ("******************************************************")