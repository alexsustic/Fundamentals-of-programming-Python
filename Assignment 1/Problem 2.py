"""
Checks if a number is prime or not
"""
def isPrime(number):
    if (number<2):
        return False
    elif(number==2):
        return True
    else:
        for i in range(2,int(number/2)):
           if (number%i==0) :
            return False
    return True



"""
Checks if a number is a Goldbach number or not
"""
def is_Goldbach_Number(number):
    if number<4:
        return False
    return True



"""
Checks if two pairs of numbers are Prime and returns their addition
"""
def sumPrime(number1,number2):
            SUM=0
            if (isPrime(number1)==True) and (isPrime(number2)==True) :
                 SUM=number1+number2
                 return SUM
def start():    
   typedNumber=int(input("Introduce the value:", ))
   if (is_Goldbach_Number(typedNumber)==True):
    for number1 in range(2,(int)(typedNumber/2)+1):
        for number2 in range((int)(typedNumber/2),typedNumber):
              if(sumPrime(number1,number2)==typedNumber):
                   print(number1,number2)
                   if (number1!=number2):
                      print(number2,number1)
   else:
      print("It's not a Goldbach number")

start()
