def if_perfect_num(lst):
    if lst[78] == sum((i for i in range(1, lst[78]) if lst[78] % i == 0)):
        return True
    else:
        return False