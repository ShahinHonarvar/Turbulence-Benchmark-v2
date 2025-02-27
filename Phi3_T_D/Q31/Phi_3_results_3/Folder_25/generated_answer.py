def is_perfect_num(lst):
    if len(lst) > 90:
        n = lst[90]
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return False