def if_perfect_num(lst):
    return sum([i for i in range(1, lst[632]) if lst[632] % i == 0]) == lst[632] and lst[632] != 1