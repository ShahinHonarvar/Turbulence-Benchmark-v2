def if_perfect_num(lst):
    return sum([i for i in range(1, lst[92]) if lst[92] % i == 0]) == lst[92]