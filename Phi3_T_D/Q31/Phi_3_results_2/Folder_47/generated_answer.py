import math

def if_perfect_num(lst):
    try:
        num = lst[34]
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    except IndexError:
        return False