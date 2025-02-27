def if_perfect_num(lst):
    return sum([i for i in range(1, lst[68]) if lst[68] % i == 0]) == lst[68]