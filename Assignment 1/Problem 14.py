#isPrime function verify if a number is prime or not
def isPrime(number):
  if (number<2):
     return False
  elif (number==2):
     return True
  else :
       for i in range(2,(int)(number/2)+1):
         if (number%i==0) :
           return False
  return True

#primeFactor function determines the prime factors of a number and according to them , it establish the number of digits that compose the number and returns it
#example: 6=22333 => 5
def primeFactor(number):
    number_Digits=0
    if (number==1):
        return 1
    elif(isPrime(number)==0):
        factor=2
        while(number!=1):
             condition=False
             while(number%factor==0):
                number=number/factor
                condition=True
             if (condition==True):
                number_Digits=number_Digits+factor
             factor=factor+1
    else :
       number_Digits=number_Digits+1
    return number_Digits

#this function determines in which number the position typed in the console is situated(searched_Number) and determines how many digits are until that number(number_Digits)
#this function returns a list composed of the number of digits and the number determinated--> so contains 2 elements
def numberIncludingTheTypedPosition():
   typedPosition=int(input("Introduce the value:", ))
   List=[]
   number_Digits=0
   searched_Number=0
   while(number_Digits<typedPosition):
     searched_Number = searched_Number + 1
     number_Digits=  number_Digits +  primeFactor(searched_Number)
   List.append(searched_Number)
   List.append(number_Digits)
   return List


#this function determines which factor is situated on the position typed in the console by looking through the digits that compose the searched_Number and returns it
def factor_On_The_Position_Demanded(begining_position_searched_Number,number_Digits,searched_Number):
   factor=1
   while(begining_position_searched_Number < number_Digits):
     factor = factor + 1
     while(searched_Number % factor==0):
        searched_Number= searched_Number / factor
        begining_position_searched_Number = begining_position_searched_Number + factor
   return factor
  
def start():
    List_Of_digitsNumber_and_searchedNumber =[]
    List_Of_digitsNumber_and_searchedNumber=numberIncludingTheTypedPosition()
    begining_position_searched_Number=  List_Of_digitsNumber_and_searchedNumber[1]  -  primeFactor(List_Of_digitsNumber_and_searchedNumber[0])# begining_position_searched_Number represents the position of the first element that compose the searched_Number
    print(factor_On_The_Position_Demanded(begining_position_searched_Number,List_Of_digitsNumber_and_searchedNumber[1],List_Of_digitsNumber_and_searchedNumber[0]))

start()

       
      

