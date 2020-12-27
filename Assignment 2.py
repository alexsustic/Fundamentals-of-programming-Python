import math
def setNumberRealPart(list, number):
    list[0]=number

def setNumberImaginaryPart(list, number):
    list[1]=number

def getNumberRealPart(number):
    return number[0]

def getNumberImaginaryPart(number):
    return number[1]

"""
    input: real, imaginary - the real and imaginary part of a number
    output: the number, as an element of the list
"""
def createNumber(realPart=0, imaginaryPart=0):
    complexNumber = [0, 0]
    setNumberRealPart(complexNumber, realPart)
    setNumberImaginaryPart(complexNumber, imaginaryPart)
    return complexNumber

"""
    Fills the list of numbers with ten given values already available at program startup
"""
def initialNumberList():
    numberList = []
    numberList.append(createNumber(2, 3))
    numberList.append(createNumber(5, -5))
    numberList.append(createNumber(-8, 6))
    numberList.append(createNumber(-3, 4))
    numberList.append(createNumber(1, -10))
    numberList.append(createNumber(2, 27))
    numberList.append(createNumber(1, 11))
    numberList.append(createNumber(6, 8))
    numberList.append(createNumber(3, 4))
    numberList.append(createNumber(-6, -8))
    return numberList



"""
    This is the console interface
"""
def print_menu():
    print("1. Read number")
    print("2. Display list")
    print("3. The sequence in which the difference between the modulus of consecutive numbers is a prime number")
    print("4. The sequence of distinct numbers")
    print("5. Exit")

    
   
"""
    Through this function , the numbers are displayed in a+bi form
"""
def display_list(list):
   for i in range (0,len(list)):
        if(list[i][1]>=0):
          print(list[i][0],"+",list[i][1],"i")
        else:
          print(list[i][0],"-",abs(list[i][1]),"i")
          

"""
    Reads a numbers and adds it to the list
"""
def readNumber(list):
    realPart = int(input("Insert real part: "))
    imaginaryPart = int(input("Insert imaginary part: "))
    list.append(createNumber(realPart, imaginaryPart))
    

    
"""
   Looks for the longest sequence in which the difference between the modulus of consecutive numbers is a prime number and returns it
"""
def Modulus_Difference_Consecutive_Numbers_is_Prime_Sequence(list):
    sequenceLenght=0
    sequence=[]
    longestSequence=[]
    maximumValue=0
    for i in range (0,len(list)-1):
        modulus1=(int)(math.sqrt(list[i][0]*list[i][0]+list[i][1]*list[i][1]))
        modulus2=(int)(math.sqrt(list[i+1][0]*list[i+1][0]+list[i+1][1]*list[i+1][1]))
        if((isPrime(abs(modulus1-modulus2))==True) and (modulus1*modulus1==list[i][0]*list[i][0]+list[i][1]*list[i][1]) and (modulus2*modulus2==list[i+1][0]*list[i+1][0]+list[i+1][1]*list[i+1][1])):
            if (sequenceLenght==0):
              sequence.append(list[i])
              sequence.append(list[i+1])
              sequenceLenght=sequenceLenght+2

            else :
              sequence.append(list[i+1])
              sequenceLenght=sequenceLenght+1

            if (sequenceLenght > maximumValue):
                maximumValue = sequenceLenght
                longestSequence = sequence.copy()
        else :
             sequence.clear()
             sequenceLenght=0
    return longestSequence

"""
Looks for the longest sequence of distinct numbers
"""
def Distinct_Number_Sequence(list):
     sequence=[]
     longestSequence=[]
     maximumValue=0
     lenght=0
     for i in range (0,len(list)):
       verificationVariable=True
       for j in range (0,len(list)):
         if (i==j):
           j=j+1
         else:
            if((list[i][0]==list[j][0]) and (list[i][1]==list[j][1])):
                verificationVariable=False
                if (lenght>maximumValue):
                   longestSequence=sequence.copy()
                   maximumValue=lenght
                lenght=0
                sequence.clear()
       if (verificationVariable==True):
            sequence.append(list[i])
            lenght=lenght+1
     if(maximumValue==0):
       return sequence
     return longestSequence


"""
  Check if a number is prime or not( returns a boolean value: True/False)
"""
def isPrime(number):
    if (number<2):
        return False
    elif(number==2):
        return True
    else:
       for i in range(2,(int)(number/2)+1):
           if (number%i==0):
                return False
    return True


"""
 This is the menu-console that gives instructions
"""
def start():
    listComplexNumbers = initialNumberList()
    while True:
        print_menu()
        command = int(input(">"))
        if command==1:
            readNumber(listComplexNumbers)
        elif command==2:
            display_list(listComplexNumbers)
        elif command==3:
            display_list(Modulus_Difference_Consecutive_Numbers_is_Prime_Sequence(listComplexNumbers))
        elif command==4:
            display_list(Distinct_Number_Sequence(listComplexNumbers))
        elif command==5:
            break
        else:
            print("Wrong command")
        print("")

start()
