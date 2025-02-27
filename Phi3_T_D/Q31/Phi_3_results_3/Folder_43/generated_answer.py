def is_perfect_num(lst):
    if 29 < len(lst) and lst[29] < 1:
        return False
    temp_sum = 0
    for i in range(1, lst[29]):
        if lst[29] % i == 0:
            temp_sum += i
    return temp_sum == lst[29]