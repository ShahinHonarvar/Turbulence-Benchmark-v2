def if_perfect_num(lst):
    return sum([i for i in range(1, lst[990]) if lst[990] % i == 0]) == lst[990] and lst[990] != 1