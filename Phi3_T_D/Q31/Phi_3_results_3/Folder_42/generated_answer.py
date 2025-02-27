def if_perfect_num(lst):
    if len(lst) > 275 and sum((i for i in range(1, lst[275]) if lst[275] % i == 0)) == lst[275]:
        return True
    return False