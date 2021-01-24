import readNum
import decimal
value=[]        #empty list
end=readNum.readNum(value)  
print(end)      #>> prints This list is empty however it will still return a list to avoid TypeErrors

value=float("NaN")     #NaN
end=readNum.readNum(value)  
print(end)      #>>Your value is not a number (NaN)

value=3+5j      #complex Number
end=readNum.readNum(value)  
print(end)    #>>a complex number with a real part of three and a imaginary part of five

value=3+0j    #>> a wrong complex Number
end=readNum.readNum(value)  
print(end)  #>>returns the real part

value="3"   #String of Number
end=readNum.readNum(value)  
print(end)  	#>>returns the number

value=0     #zero
end=readNum.readNum(value)  
print(end)  #>> zero

value=decimal.Decimal("3") #also supports Decimals
end=readNum.readNum(value)  
print(end)  

value=decimal.Decimal("3.450") #cuts over-standing zeros
end=readNum.readNum(value)  
print(end)

value=3.1034394123  	#reads floats almost always exactly
end=readNum.readNum(value)  
print(end)

value=10*10**210    #too long numbers do not give an error but tell you peacefully
end=readNum.readNum(value)  
print(end)        

value=1*10**23     #reads ints up to a length of 24
end=readNum.readNum(value)  
print(end)      #one hundred sextillion

value=0.00000051       #reads small floats too, up to a length of 8!
end=readNum.readNum(value)  
print(end)

value={1:[1,2,3],2:(9,4),6:{3:[2,5,6],9:[23,89]}}
end=readNum.readNum(value)  
print(end)      #will give you the exact same structure back 

#some tests with random ints
value=0.00000051       #reads small floats too, up to a length of 8!
end=readNum.readNum(value)  
print(end)

readNum.setPrecision(2)
value=-0.00000051       #reads negative floats too
end=readNum.readNum(value)  
print(end)          #negative +float


#try random ints from random.org between max and min

value=814524359       
end=readNum.readNum(value)  
print(end)

value=341328995        
end=readNum.readNum(value)  
print(end)

value=100411938 
end=readNum.readNum(value)  
print(end)

value=316023361         
end=readNum.readNum(value)  
print(end) 

print("Finished successfully")

