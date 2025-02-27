def if_perfect_num(lst):
    if 53 < len(lst) and lst[53] > 1:
        n = lst[53]
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return False