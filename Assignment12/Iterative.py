vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



def display_vector(n):
    for index in range(1, n + 1):
        print(vector[index], end=" ")
    print('')


def validation(number, m):
    index = 0
    boolean_value = True
    for index in range(1, number):
        if vector[number] == vector[index]:
            boolean_value = False
    if index > 0:
        if abs(vector[index + 1] - vector[index]) < m:
            return False
    return boolean_value

def solution(n, m):
    index = 1
    vector[index] = 0
    while index > 0:
        if vector[index] < n:
            vector[index] += 1
            if validation(index, m):
                if index == n:
                    display_vector(n)
                    vector[0] += 1
                else:
                    index += 1
                    vector[index] = 0
        else:
            index -= 1
    return vector[0]
#verify is all there are elements equal with vect[number] from 0 to number and if the modul is smaller
#if the validation true makes the next element 0 and increment index
#false, inc 

def main_iterative():
    n = int(input("Insert the value of n: "))
    m = int(input("Insert the value of m: "))
    number_of_solutions = solution(n, m)
    if number_of_solutions == 0:
        print("Inexistent solutions!")

