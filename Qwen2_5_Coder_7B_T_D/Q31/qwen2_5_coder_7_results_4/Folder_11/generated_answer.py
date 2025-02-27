def if_perfect_num(lst):
    return lst[77] == sum([i for i in range(1, lst[77]) if lst[77] % i == 0])