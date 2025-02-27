def if_perfect_num(lst):
    if len(lst) > 29 and lst[29] == sum((i for i in range(1, lst[29]) if lst[29] % i == 0)):
        return True
    else:
        return False