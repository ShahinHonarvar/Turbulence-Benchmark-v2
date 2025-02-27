def if_perfect_num(lst):
    return lst[45] == sum([i for i in range(1, lst[45]) if lst[45] % i == 0])