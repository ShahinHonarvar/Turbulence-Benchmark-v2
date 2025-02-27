def sum_of_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])

def if_perfect_num(lst):
    if len(lst) > 64:
        return sum_of_divisors(lst[64]) == lst[64]
    else:
        return False