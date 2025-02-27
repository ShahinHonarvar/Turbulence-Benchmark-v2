def if_perfect_num(lst):
    return sum([i for i in range(1, lst[453]) if lst[453] % i == 0]) == lst[453] and lst[453] != 1