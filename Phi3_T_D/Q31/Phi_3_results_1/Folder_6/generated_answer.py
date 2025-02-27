def if_perfect_num(lst):
    n = lst[790]
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n and 1 in divisors