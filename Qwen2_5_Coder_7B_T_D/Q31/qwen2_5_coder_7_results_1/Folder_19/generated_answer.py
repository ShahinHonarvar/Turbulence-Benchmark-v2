def if_perfect_num(lst):
    return sum(lst[12]) == sum([i for i in range(1, lst[12]) if lst[12] % i == 0])