def if_perfect_num(lst):
    return sum([i for i in range(1, lst[54]) if lst[54] % i == 0]) == lst[54]