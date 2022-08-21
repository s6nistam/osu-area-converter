def Inputvalues():
    print("please enter your Tablet Area in the following format: up,down,left,right (for example 0,4700,0,8500)")
    valueinput = input()
    return valueinput.split(',')

def checkvalidity(values):
    if len(values) != 4:
        print("wrong number of inputs")
        return False
    try: values = [float(value) for value in values]
    except: 
        print("input was not convertible to float")
        return False
    if values[0] > values[1]: 
        print("invalid value for up. up must be smaller than down")
        return False
    if values[2] > values[3]: 
        print("invalid value for left. left must be smaller than right")
        return False
    return True

def calculate(values):
    values = [float(value) for value in values]
    width = (values[3] - values[2])/100
    print("width = {0}".format(width))
    height = (values[1] - values[0])/100
    print("height = {0}".format(height))
    X = values[2]/100 + width/2
    print("X offset = {0}".format(X))
    Y = values[0]/100 + height/2
    print("Y offset = {0}".format(Y))