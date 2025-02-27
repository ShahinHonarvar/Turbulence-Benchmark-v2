from math import sqrt

def is_perfect(n):
    sum_of_factors = 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            sum_of_factors += i
            if i != n // i:
                sum_of_factors += n // i
    return sum_of_factors == n

def if_perfect_num(numbers):
    return is_perfect(numbers[24]) if len(numbers) > 24 else False