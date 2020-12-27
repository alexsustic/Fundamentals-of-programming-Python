vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def solution(number, n, m):
    for first_index in range(1, n + 1):
        vector[number] = first_index
        if validation(number, m):
            if number == n:
                vector[0] += 1
                for second_index in range(1, n + 1):
                    print(vector[second_index], end=" ")
                print("")
            else:
                solution(number + 1, n, m)
    return vector[0]

def validation(number, m):
    for index in range(1, number):
        if vector[number] == vector[index]:
            return False
        if number > 1:
            if abs(vector[number] - vector[number - 1]) < m:
                return False
    return True


def main_recursive():
    n = int(input("Insert the value of n: "))
    m = int(input("Insert the value of m: "))
    number_of_solutions = solution(1, n, m)
    if number_of_solutions == 0:
        print("Inexistent solutions!")
