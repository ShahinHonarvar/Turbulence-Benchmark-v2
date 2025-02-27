def if_perfect_num(lst):
    return sum((lst[78] // i for i in range(1, int(lst[78] ** 0.5) + 1) if lst[78] % i == 0)) == lst[78]