def if_perfect_num(lst):
    if lst[1] == sum([i for i in range(1, lst[1]) if lst[1] % i == 0]):
        return True
    else:
        return False