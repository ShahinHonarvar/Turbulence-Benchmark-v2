def if_perfect_num(lst):
    return sum((i for i in range(1, 790) if 790 % i == 0)) == 790