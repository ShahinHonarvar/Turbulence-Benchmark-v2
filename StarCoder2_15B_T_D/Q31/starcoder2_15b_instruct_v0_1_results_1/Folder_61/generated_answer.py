def if_perfect_num(lst):
    if lst[8] == sum((i for i in range(1, lst[8]) if lst[8] % i == 0)):
        return True
    return False