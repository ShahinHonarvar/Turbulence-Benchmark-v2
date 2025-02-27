def if_perfect_num(lst):
    if len(lst) <= 321:
        return False
    n = lst[321]
    return sum((i for i in range(1, n) if n % i == 0)) == n