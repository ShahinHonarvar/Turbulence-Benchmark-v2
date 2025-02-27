def if_perfect_num(lst):
    n = lst[478]
    return n == sum((i for i in range(1, n) if n % i == 0))