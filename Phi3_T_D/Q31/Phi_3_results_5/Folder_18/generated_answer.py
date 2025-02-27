def if_perfect_num(integers):
    n = integers[312]
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n