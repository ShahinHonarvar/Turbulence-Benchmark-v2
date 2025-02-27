def if_perfect_num(lst):
    return sum((lst[194] // i for i in range(1, int(lst[194] ** 0.5) + 1) if lst[194] % i == 0)) == lst[194] and lst[194] != 1