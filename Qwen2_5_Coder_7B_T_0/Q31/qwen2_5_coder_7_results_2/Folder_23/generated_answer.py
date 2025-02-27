def if_perfect_num(lst):
    return sum([i for i in range(1, lst[69]) if lst[69] % i == 0]) == lst[69] and lst[69] != 1