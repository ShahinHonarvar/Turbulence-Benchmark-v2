def is_perfect_num(lst):
    if len(lst) > 41 and lst[41] % sum(set(divisors(lst[41]))) == 0:
        return True
    return False

def divisors(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]