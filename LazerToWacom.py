def Inputvalues():
    print("please enter your Tablet Area in the following format: width,height,X Offset,Y Offset (for example 85,47,42.5,23.5)")
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
    if values[2] < values[0]/2: 
        print("Area too far left, try increasing the X Offset")
        return False
    if values[3] < values[1]/2: 
        print("Area too far up, try increasing the Y Offset")
        return False
    return True

def calculate(values):
    values = [float(value) for value in values]
    up = (values[2] - values[0]/2) * 100
    print("up = {0}".format(up))
    down = up + (values[1] * 100)
    print("down = {0}".format(down))
    left = (values[3] - values[1]/2) * 100
    print("left = {0}".format(left))
    right = left + (values[0] * 100)
    print("right = {0}".format(right))