import argparse

def RoundUp(x):
    if x == int(x): return x
    else: return int((x + 1))

def SelectDirection():
    print("Do you want to convert from Wacom to OpenTabletDriver/OsuLazerInBuilt (input 1), OTD/Lazer to Wacom (input 2), Wacom to OTD/Lazer with forced Aspect Ratio (input 3)")
    return input()

def InputvaluesWacom():
    print("please enter your Tablet Area in the following format: up,down,left,right (for example 0,4700,0,8500)")
    valueinput = input()
    return valueinput.split(',')

def checkvalidityWacom(values):
    if len(values) != 4:
        print("wrong number of inputs")
        return False
    try: values = [int(value) for value in values]
    except: 
        print("input was not convertible to int")
        return False
    if values[0] > values[1]: 
        print("invalid value for up. up must be smaller than down")
        return False
    if values[2] > values[3]: 
        print("invalid value for left. left must be smaller than right")
        return False
    return True

def WacomToLazer(values):
    width = round((values[3] - values[2])/100)
    print("width = {0}".format(width))
    height = round((values[1] - values[0])/100)
    print("height = {0}".format(height))
    X = RoundUp(values[2]/100 + width/2)
    print("X offset = {0}".format(X))
    Y = RoundUp(values[0]/100 + height/2)
    print("Y offset = {0}".format(Y))

def InputvaluesLazer():
    print("please enter your Tablet Area in the following format: width,height,X Offset,Y Offset (for example 85,47,42.5,23.5)")
    valueinput = input()
    return valueinput.split(',')

def checkvalidityLazer(values):
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

def LazerToWacom(values):
    up = round((values[2] - values[0]/2) * 100)
    print("up = {0}".format(up))
    down = round(up + (values[1] * 100))
    print("down = {0}".format(down))
    left = round((values[3] - values[1]/2) * 100)
    print("left = {0}".format(left))
    right = round(left + (values[0] * 100))
    print("right = {0}".format(right))

def InputvaluesWacomFA():
    print("please enter your Tablet Area in the following format: up,down,left,right,Aspect Ratio(X:Y) (for example 0,4700,0,8500,85:47)")
    valueinput = input()
    valuessplit = valueinput.split(',')
    return [valuessplit[i] for i in range(len(valuessplit) - 1)] + [valuessplit[len(valuessplit) - 1].split(':')[i] for i in range(2)]

def checkvalidityWacomFA(values):
    if len(values) != 6:
        print("wrong number of inputs")
        return False
    try: values = [int(values[i]) for i in range(6)]
    except: 
        print("input was not convertible to int")
        return False
    if values[0] > values[1]: 
        print("invalid value for up. up must be smaller than down")
        return False
    if values[2] > values[3]: 
        print("invalid value for left. left must be smaller than right")
        return False
    return True

def WacomToLazerFA(values):
    c = values[4]/values[5]
    height = round((values[1] - values[0])/100)
    width = round(c * height)
    X = RoundUp(values[2]/100 + width/2)
    Y = RoundUp(values[0]/100 + height/2)
    print("width = {0}".format(width))
    print("height = {0}".format(height))
    print("X offset = {0}".format(X))
    print("Y offset = {0}".format(Y))

parser = argparse.ArgumentParser(description = "Converts Wacom Tablet Areas to or from OpenTabletDriver/Lazer Areas")
parser.add_argument('-mode', metavar = 'mode', type = int, help = '1 = Wacom to OTP/Lazer, 2 = OTD/Lazer to Wacom, 3 = Wacom to OTD/Lazer with forced aspect ratio')
parser.add_argument('-values', metavar = 'values', type = str, help = 'mode 1: up,down,left,right (for example 0,4700,0,8500) mode 2: width,height,X Offset,Y Offset (for example 85,47,42.5,23.5) mode 3: up,down,left,right,Aspect Ratio(X:Y) (for example 0,4700,0,8500,85:47)')
args = parser.parse_args()
selection = ""
values = []
if args.mode != None and args.values != None:
    selection = args.mode
    values = args.values.split(',')
    if selection == 1:
        if checkvalidityWacom(values):
            values = [int(value) for value in values]
            WacomToLazer(values)
    elif selection == 2:
        if checkvalidityLazer(values):
            values = [float(value) for value in values]
            LazerToWacom(values)
    else:
        values = [values[i] for i in range(len(values) - 1)] + [values[len(values) - 1].split(':')[i] for i in range(2)]
        if checkvalidityWacomFA(values):
            values = [int(values[i]) for i in range(6)]
            WacomToLazerFA(values)
else:
    selection = SelectDirection()
    error = False
    try: selection = int(selection)
    except: error = True
    if selection not in [1,2,3]:
        error = True
    while error:
        print("error. please try again.")
        selection = SelectDirection()
        try: selection = int(selection)
        except: pass
        if selection in [1,2,3]:
            error = False
    if selection == 1:
        values = InputvaluesWacom()
        if checkvalidityWacom(values):
            values = [int(value) for value in values]
            WacomToLazer(values)
    elif selection == 2:
        values = InputvaluesLazer()
        if checkvalidityLazer(values):
            values = [float(value) for value in values]
            LazerToWacom(values)
    else:
        values = InputvaluesWacomFA()
        if checkvalidityWacomFA(values):
            values = [int(values[i]) for i in range(6)]
            WacomToLazerFA(values)
print("press enter to close")
input()