def if_perfect_num(lst):
    if lst[247] == sum([i for i in range(1, lst[247]) if lst[247] % i == 0]):
        return True
    else:
        return False