def if_perfect_num(lst):
    return sum([i for i in range(1, lst[45]) if lst[45] % i == 0]) == lst[45] and lst[45] != 1