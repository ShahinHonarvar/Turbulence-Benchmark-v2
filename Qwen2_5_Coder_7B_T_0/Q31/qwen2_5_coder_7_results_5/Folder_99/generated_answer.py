def if_perfect_num(lst):
    return sum([i for i in range(1, lst[733]) if lst[733] % i == 0]) == lst[733]