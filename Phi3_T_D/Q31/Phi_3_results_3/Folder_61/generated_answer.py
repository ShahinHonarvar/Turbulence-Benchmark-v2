def if_perfect_num(lst):
    if len(lst) > 8:
        n = lst[8]
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return False