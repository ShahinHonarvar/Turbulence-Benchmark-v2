def if_perfect_num(lst):
    return sum([i for i in range(1, lst[97]) if lst[97] % i == 0]) == lst[97]