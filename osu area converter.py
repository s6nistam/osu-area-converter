import argparse

import WacomToLazer as wtl
import LazerToWacom as ltw
import WacomToLazerFA as wtlfa

def SelectDirection():
    print("Do you want to convert from Wacom to OpenTabletDriver/OsuLazerInBuilt (input 1), OTD/Lazer to Wacom (input 2), Wacom to OTD/Lazer with forced Aspect Ratio (input 3)")
    return input()

parser = argparse.ArgumentParser(description = "Converts Wacom Tablet Areas to or from OpenTabletDriver/Lazer Areas")
parser.add_argument('-mode', metavar = 'mode', type = int, help = '1 = Wacom to OTP/Lazer, 2 = OTD/Lazer to Wacom, 3 = Wacom to OTD/Lazer with forced aspect ratio')
parser.add_argument('-values', metavar = 'values', type = str, help = 'mode 1: up,down,left,right (for example 0,4700,0,8500) mode 2: width,height,X Offset,Y Offset (for example 85,47,42.5,23.5) mode 3: up,down,left,right,Aspect Ratio(X:Y) (for example 0,4700,0,8500,85:47)')
args = parser.parse_args()
selection = ""
values = []
if args.mode != None and args.values != None:
    selection = args.mode
    values = args.values.split(',')
    module = None
    if selection == 1:
        module = wtl
    elif selection == 2:
        module = ltw
    else:
        module = wtlfa
    if module.checkvalidity(values):
            module.calculate(values)
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
        module = wtl
    elif selection == 2:
        module = ltw
    else:
        module = wtlfa
    values = module.Inputvalues()
    if module.checkvalidity(values):
            module.calculate(values)
    print("press enter to close")
    input()