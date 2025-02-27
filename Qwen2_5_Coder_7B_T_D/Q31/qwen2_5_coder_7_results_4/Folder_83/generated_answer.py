def if_perfect_num(lst):
    return sum((lst[95] // i for i in range(1, int(lst[95] ** 0.5) + 1) if lst[95] % i == 0)) == lst[95]