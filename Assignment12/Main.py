from Assignment12.Iterative import main_iterative
from Assignment12.Recursive import main_recursive

def printMenu():
    print("1.Iterative method")
    print("2.Recursive method")
    print("3.Exit")
def run():
    printMenu()
    while True:
        command = input("What type of method would you like to choose:")
        if command == '1':
            main_iterative()
        elif command == '2':
            main_recursive()
        else:
            break

run()