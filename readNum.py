import math
from numbers import Number
import decimal as decimals

_maxDecimalLength=8
def setPrecision(integer):
    _maxDecimalLength=integer
def readNum(value):
    try:
        value
        if value is None:         #none
            return ("Your value is none")
        elif isinstance(value,tuple):
            if value:   #basically if not empty
                output=[]
                #print("Converting " +value.__class__.__name__+ " to list ...")
                for x in value:
                    output.append(readNum(x))
                return output
            else:
                pass
                #print("This "+value.__class__.__name__+" is empty")
        elif isinstance(value,list):
            if value:   #basically if not empty
                output=[]
                #print("Converting " +value.__class__.__name__+ " to list ...")
                for x in value:
                    output.append(readNum(x))
                return output
            else:
                pass
                #print("This "+value.__class__.__name__+" is empty")
        elif isinstance(value,dict):
            if value:   #basically if not empty
                output=[]
                #print("Converting " +value.__class__.__name__+ " to list ...")
                for x in value:
                    output.append(readNum(value[x]))
                return output
            else:
                pass
                #print("This "+value.__class__.__name__+" is empty")
        elif isinstance(value,set):
            if value:   #basically if not empty
                output=[]
                #print("Converting " +value.__class__.__name__+ " to list ...")
                for x in value:
                    output.append(readNum(x))
                return output
            else:
                pass
                #print("This "+value.__class__.__name__+" is empty")
        elif isinstance(value,Number): 
            if isinstance(value,decimals.Decimal):
                if not value==int(value):   #real Decimal
                    return readDecimal(value)   #this has to be the only read Decimal in the code instead redirect to readNum(Decimal(value))
                else:               #Int
                    return readInt(int(value))
            elif isinstance(value,complex):
                if value.imag:
                    return("a complex number with a real part of "+readNum(value.real)+" and a imaginary part of "+readNum(value.imag))
                else:
                    try:
                        return readNum(value.real)
                    except:
                        return ("There was a problem with your complex number. Do not use complex numbers with empty imaginary parts")
            elif len(str(value))>32:
                return ("This number is too long") 
            elif math.isnan(value): #nan
                return ("Your value is not a number (NaN)")
            elif isinstance(value,float):
                if not value.is_integer() and not value==int(value): #real float
                    return readNum(decimals.Decimal.from_float(value))
                else:   #integer
                    return readInt(int(value))
            elif isinstance(value,int):     #int
                return readInt(value)
        elif isinstance(value,str):
                try:
                    return readNum(decimals.Decimal(value))
                except:
                    if value.isnumeric():
                        try:
                            return readNum(int(value))
                        except:
                            try:
                                return readNum(complex(value))
                            except:
                                return ("This is a String that is not convertible into a number")
                    else:
                        return  "This is a String that is not a number"
    except NameError: #undefined
        raise Exception("Your value is undefined")
    return value

def readInt(value):
    output=[]
    if value<0:
        output.append("minus")
        value=-value
    local=str(value)   #string representation  
    length=len(local)  #if value is dynamic define a max length instead. 
    if length > 24:
        return ("This int is too long")
    numbers=[]
    for i in range(3): 
        numbers.insert(i,_getSingleToString())
    numbers[1][2]="twen";numbers[1][3]="thir";numbers[1][4]="for";numbers[1][5]="fif";numbers[1][8]="eigh";numbers[1][9]="nin"
    strings=["", "ty"," hundred"]
    nextLevel=[" ","thousand","million","billion","trillion","quadrillion","quintillion","sextillion"] #and so on 
    array=[] #array representation
    lengthArr=math.ceil(length/3)
    for j in range(lengthArr):
        array.insert(j,[0]*3)
    maxL=lengthArr*3
    for i in range(maxL): 
        icorrect=i-maxL+length #the position of the 3 in 3027 has to be 2 instead of 0
        Pos1=math.floor(i/3)
        Pos2=i%3
        if icorrect<0:
            array[Pos1][Pos2]=0  #filling all empty spaces or 0s with 0
        else:
            array[Pos1][Pos2]=int(local[icorrect]) #makes an int from the string at position i #now the array looks like this [5,1,3],[6,9,0]
    if value==0:
        output=["zero"]
    else:
        for i in range(lengthArr):
            inside=False
            if array[i][1]==1:
                teenSwitch = {
                    0:"ten",
                    1:"eleven",
                    2:"twelve",
                    3:"thirteen",
                    5:"fifteen"
                } # this could have been implemented more efficiently maybe (see default)
                teen=teenSwitch.get(array[i][2],numbers[2][array[i][2]]+"teen")
                output.extend([numbers[2][array[i][0]]+strings[2],teen])
            else:
                for j in range(3):
                    if not array[i][j]: #it might be (undefined or) 0 like in 003457
                        continue 
                    else:
                        output.extend([numbers[2-j][array[i][j]]+strings[2-j]])
                        inside=True
            if inside:
                output.append(nextLevel[lengthArr-i-1])
        for i in range(len(output)):
            if output[i]=="":
                output[i]=None
    return (' '.join(output)).strip()

def readDecimal(decBig): #only give a decimal
    decimals.getcontext().prec = _maxDecimalLength
    output=[]
    single=_getSingleToString()
    single[0]="zero"
    try:
        if isinstance(decBig,decimals.Decimal):
            pass
        else:
            return readNum(int(decBig))
    except NameError:
        raise Exception("Not defined"+str(type(decBig)))
    #decBig has an int component and a decimal places component
    intPart=int(decBig)
    if intPart==0 and decBig<0:
        output.append("negative")
    output.append(readInt(intPart))
    output.append("point")
    decimalPart=abs(decBig-intPart)
    decStr=str(decimalPart)
    isE=decStr.find('E')
    if (isE != -1): #format x.yz00000E-a
        Correct=decStr[-1:] #a
        decStr=decStr[:isE].replace(".","")
        zeroes=""
        for i in range(int(Correct)):
            zeroes=zeroes+str("0")
        decStr=zeroes+decStr
    else:       #format 0.xyz
        decStr=decStr[2:] #0.xyz is supposed to be xyz so cut the first two digits
    length=len(decStr)
    for x in decStr: 
        try:
            output.append(single[int(x)])
        except TypeError:
            pass
            #print("Some insignificant problem occured: Still running")
        except ValueError:
            pass
            #print("E couldn't be cast to an integer")
    length=len(output)
    for i in range(length-1,-1,-1):
        if output[i]=="zero" and i>0:
            del output[i]
        else:
            break
    return " ".join(output)

def _getSingleToString():
    return ["","one","two","three","four","five","six","seven","eight","nine"]
    

