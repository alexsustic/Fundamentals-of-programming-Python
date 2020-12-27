"""
the Fibonacci function generates into the list f ,all the numbers from The Fibonacci sequence until it meets the first value greater than n and returns it
"""
def Fibonacci(greaterThanThisNumber):
    fibonacci_Sequence=[]
    fibonacci_Sequence.append(1)
    fibonacci_Sequence.append(1)
    i=1
    while(fibonacci_Sequence[i]<=greaterThanThisNumber) :
        i=i+1
        fibonacci_Sequence.append(fibonacci_Sequence[i-1]+fibonacci_Sequence[i-2])
    last_element_generated=fibonacci_Sequence[i]
    return last_element_generated

def start():
  greaterThanThisNumber=int(input("Introduce the value:", ))
  print(Fibonacci(greaterThanThisNumber))
  
start()
