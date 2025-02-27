def if_perfect_num(lst):
    return sum([i for i in range(1, lst[47]) if lst[47] % i == 0]) == lst[47]