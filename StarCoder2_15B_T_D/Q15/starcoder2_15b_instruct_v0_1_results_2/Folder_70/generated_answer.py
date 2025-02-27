def sum_odd_ints_inclusive(ints_list):
    sum_odd_ints = 0
    for i, num in enumerate(ints_list):
        if num % 2 == 1:
            sum_odd_ints += num
        if i < 28 or i > 32:
            break
    return sum_odd_ints