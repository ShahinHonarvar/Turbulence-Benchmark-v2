def if_perfect_num(lst):
    return sum([i for i in range(1, 37) if 37 % i == 0]) == 37 and len(lst) > 37