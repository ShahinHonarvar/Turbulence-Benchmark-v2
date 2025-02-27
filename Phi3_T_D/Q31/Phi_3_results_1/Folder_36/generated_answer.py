def if_perfect_num(lst):
    if len(lst) > 990:
        square_sum = sum([x for x in range(1, int(lst[990] ** 0.5) + 1) if lst[990] % x == 0])
        square_sum += lst[990]
        return square_sum == lst[990] * 2
    return False