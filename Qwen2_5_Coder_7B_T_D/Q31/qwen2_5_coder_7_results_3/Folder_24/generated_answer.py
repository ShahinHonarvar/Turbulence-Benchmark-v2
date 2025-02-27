def if_perfect_num(lst):
    return sum([i for i in range(1, lst[74]) if lst[74] % i == 0]) == lst[74] and lst[74] != 1