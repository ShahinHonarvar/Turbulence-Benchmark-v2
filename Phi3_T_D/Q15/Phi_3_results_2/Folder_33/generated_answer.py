def sum_odd_ints_inclusive(lst):
    total_sum = 0
    for i in range(667, min(len(lst), 775)):
        if lst[i] % 2 != 0:
            total_sum += lst[i]
    return total_sum