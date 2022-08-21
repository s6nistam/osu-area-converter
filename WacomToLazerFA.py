def Inputvalues():
    print("please enter your Tablet Area in the following format: up,down,left,right,Aspect Ratio(X:Y) (for example 0,4700,0,8500,85:47)")
    valueinput = input()
    values = valueinput.split(',')
    return values

def checkvalidity(values):
    if len(values) != 5:
        print("wrong number of inputs")
        return False
    try: values = [values[i] for i in range(len(values) - 1)] + [values[len(values) - 1].split(':')[i] for i in range(2)]
    except:
        print("Aspectratio was given in the wrong format")
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
    values = [float(values[i]) for i in range(len(values) - 1)] + [float(values[len(values) - 1].split(':')[i]) for i in range(2)]
    c = values[4]/values[5]
    height = (values[1] - values[0])/100
    width = c * height
    X = values[2]/100 + width/2
    Y = values[0]/100 + height/2
    print("width = {0}".format(width))
    print("height = {0}".format(height))
    print("X offset = {0}".format(X))
    print("Y offset = {0}".format(Y))