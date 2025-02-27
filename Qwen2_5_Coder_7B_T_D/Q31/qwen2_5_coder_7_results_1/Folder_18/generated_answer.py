def if_perfect_num(lst):
    return sum([i for i in range(1, lst[312]) if lst[312] % i == 0]) == lst[312]