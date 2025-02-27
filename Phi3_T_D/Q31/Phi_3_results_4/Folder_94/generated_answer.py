def is_perfect_num(lst):
    if len(lst) > 93:
        n = lst[93]
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return False