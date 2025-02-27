def if_perfect_num(lst):
    if 88 < len(lst):
        n = lst[88]
        divisors = [i for i in range(1, n // 2 + 1) if n % i == 0]
        return sum(divisors) == n
    return False