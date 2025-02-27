def if_perfect_num(lst):
    return sum([i for i in range(1, 59) if 59 % i == 0]) == 59