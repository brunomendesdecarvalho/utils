# coding: utf-8

# |~-*- Coded by: Bruno Mendes de Carvalho Castelo Branco -*-~|


def sequence(start, finish, step):
    sequence = []
    if start < finish:
        for i in range(start, finish + 1, step):
            sequence.append(i)
    
    elif start >= finish:
        for i in range(start, finish - 1, -step):
            sequence.append(i)
    
    return sequence


print(sequence(2, 10, 2))

def factorial(number):

    if number == 1 or number == 0:
        
        return 1
    
    else:
        factorial = 1
        for i in range(1, number+1):
            factorial *= i
        
        return factorial


def arithmetic_progression(start, limit, ratio):
    progression = []
    for i in range(start, limit + 1, ratio):
        progression.append(i)
    return progression


def sum_arithmetic(first, last, quantity):
    return ((first + last) * quantity) / 2


def geometric_progression(start, limit, ratio):
    progression = [start]
    term = start * ratio
    progression.append(term)

    while term < limit:
        term *= ratio
        progression.append(term)
    return progression
        

def sum_geometric_finite(first, ratio, quantity):
    return (first * (ratio ** quantity - 1)) / (ratio - 1)

def sum_geometric_infinite(first, ratio):
    if -1 < ratio < 1:
        return (first) / (1 - ratio)
    else:
        print('Invalid ratio! Must be between -1 and 1.')


def is_prime(number):
    from math import sqrt
    
    root = int(sqrt(number))
    for d in range(2, root + 1):
        if number % d == 0:
            return False
        
    return True


def higher_number(quantity):
    higher = 0
    for i in range(0, quantity):
        number = int(input('Type a number: '))
        higher = (number + higher + abs(number - higher)) / 2
    return higher


def triangle_numbers(quantity):
    sequence = []
    for i in range(1, quantity+1):
        number = int((i * (i+1)) / 2)
        sequence.append(number)
    return sequence

print(triangle_numbers(7))


def find_x(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta > 0:
        delta = delta ** 0.5
        return (-b + delta) / (2 * a), (-b - delta) / (2 * a)

    elif delta == 0:
        return -b / (2 * a)

    elif delta < 0:
        return('Delta is negative! No Xes on real dominion')


