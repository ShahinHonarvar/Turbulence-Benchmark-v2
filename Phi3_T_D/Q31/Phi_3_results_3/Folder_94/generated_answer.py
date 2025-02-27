def if_perfect_num(lst):
    if len(lst) > 93 and is_perfect(lst[93]):
        return True
    return False

def is_perfect(n):
    sum_of_divisors = sum([i for i in range(1, n) if n % i == 0])
    return sum_of_divisors == n