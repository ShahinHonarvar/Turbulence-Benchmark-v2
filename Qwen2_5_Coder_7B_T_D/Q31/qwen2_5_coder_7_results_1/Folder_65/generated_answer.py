def if_perfect_num(lst):
    return sum([i for i in range(1, lst[35]) if lst[35] % i == 0]) == lst[35] and lst[35] != 1