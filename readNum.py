import math
import decimal as decimals
from collections.abc import Iterable

decimals.getcontext().prec = 8
def readNum(value, on_nan = "Your value is not a number (NaN)"):
    if isinstance(value,(int, float, complex, decimals.Decimal)): 
        if math.isnan(value):
            return on_nan
        elif isinstance(value,decimals.Decimal):
            if not value==int(value):   #real Decimal
                return readDecimal(value)
            else:
                return readInt(int(value))
        elif isinstance(value,complex):
            try:
                return("a complex number with a real part of "+readNum(value.real)+" and an imaginary part of "+readNum(value.imag))
            except:
                raise ValueError("There was a problem with your complex number.")
        elif len(str(value))>32:
            return ("This number is too long") 
        elif isinstance(value,float):
            if not value.is_integer() and not value==int(value): #real float
                return readNum(decimals.Decimal.from_float(value))
            else:   #integer
                return readInt(int(value))
        elif isinstance(value,int):
            return readInt(value)
    elif isinstance(value, str):
        try:
            return readNum(decimals.Decimal(value))
        except ValueError:
            try:
                return readNum(complex(value))
            except:
                raise ValueError("String is not convertible into a number")
    elif isinstance(value, Iterable):
        return type(value)(map(readNum,value))
    elif isinstance(value,dict):
        return dict(
            zip(
                value.keys(),
                map(readNum,value.values())
            )
        )
    else:
        raise TypeError("Unsupported type: "+type(value).__qualname__)

def readInt(value):
    output=[]
    if value<0:
        output.append("minus")
        value=-value
    local=str(value)
    length=len(local)  
    if length > 24:
        raise ValueError("This int is too long")
    numbers=[]
    for i in range(3): 
        numbers.insert(i,_getSingleToString())
    numbers[1][2]="twen";numbers[1][3]="thir";numbers[1][4]="for";numbers[1][5]="fif";numbers[1][8]="eigh";numbers[1][9]="nin"
    strings=["", "ty"," hundred"]
    nextLevel=[" ","thousand","million","billion","trillion","quadrillion","quintillion","sextillion","septillion","octillion","nonillion","decillion","undecillion"] #and so on 
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
                }
                teen=teenSwitch.get(array[i][2],numbers[2][array[i][2]]+"teen")
                if array[i][0]==0:
                    output.extend([teen])
                else:
                    output.extend([numbers[2][array[i][0]]+strings[2],teen])
                inside=True
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

def readDecimal(decBig):
    decBig = decimals.Decimal(decBig)
    output=[]
    single=_getSingleToString()
    single[0]="zero"
    #decBig has an int component and a decimal places component
    intPart=int(decBig)
    if intPart==0 and decBig<0:
        output.append("negative")
    output.append(readInt(intPart))
    output.append("point")
    decimalPart=abs(decBig-decimals.Decimal(intPart))
    decStr=str(decimalPart)
    isE=decStr.find('E')
    if (isE != -1): #format x.yz00000E-a
        Correct=decStr[-1:] #a
        decStr=decStr[:isE].replace(".","")
        zeroes=""
        for i in range(int(Correct)-1):
            zeroes=zeroes+str("0")
        decStr=zeroes+decStr
    else:       #format 0.xyz
        decStr=decStr[2:] #0.xyz is supposed to be xyz so cut the first two digits
    length=len(decStr)
    for x in decStr: 
        output.append(single[int(x)])
    length=len(output)
    for i in range(length-1,-1,-1):
        if output[i]=="zero" and i>0:
            del output[i]
        else:
            break
    return " ".join(output)

def _getSingleToString():
    return ["","one","two","three","four","five","six","seven","eight","nine"]
    

if __name__ == '__main__':
    while True:
        a=input("Give a number? \n")
        try:
            c=readNum(eval(a))
            print(c)
        except Exception as e:
            print("Not a valid number:")
            print(e)
