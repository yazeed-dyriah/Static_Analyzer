with open("eof.txt") as file:
    lines = file.readlines()
    substring = '/'
    for i in lines:
        if not None == i and substring in i:
            divisor = i.split('/', 1)[1]
            digit = (divisor[0].isdigit())
            if int(divisor[0]) != 0:
                continue
            print("divide by zero error")
