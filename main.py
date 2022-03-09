with open("eof.txt") as file:
    lines = file.readlines()


for line in lines:
    if '==' in line and line.startswith("if") or line.startswith("else if"):
        argument = line[line.index('')]

        print("is a magic number or string")

    elif '<' in line or '>' in line or '<=' in line or '>=' in line and line.startswith("if") or line.startswith("else if"):

        print("is a magic number because include an 'operation'")

    else:

        print(" its not a magic number")
