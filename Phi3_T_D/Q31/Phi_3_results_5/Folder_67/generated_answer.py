def if_perfect_num(lst):
    if len(lst) > 43:
        for i in range(1, int(lst[43] ** 0.5) + 1):
            if lst[43] % i == 0:
                if lst[43] // i + i == lst[43]:
                    return True
        return False
    else:
        return False