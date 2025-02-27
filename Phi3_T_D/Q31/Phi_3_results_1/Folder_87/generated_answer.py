def if_perfect_num(lst):
    if 96 < len(lst):
        n = lst[96]
        divisors = [i for i in range(1, n // 2 + 1) if n % i == 0]
        return n == sum(divisors)
    return False