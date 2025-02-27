def if_perfect_num(lst):
    return sum([i for i in range(1, 993) if 993 % i == 0]) == 993