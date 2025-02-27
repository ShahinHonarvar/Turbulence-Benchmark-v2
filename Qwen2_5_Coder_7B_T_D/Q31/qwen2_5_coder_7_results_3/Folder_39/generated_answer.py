def if_perfect_num(lst):
    return sum(lst[59] == sum((i for i in range(1, lst[59]) if lst[59] % i == 0))) > 0