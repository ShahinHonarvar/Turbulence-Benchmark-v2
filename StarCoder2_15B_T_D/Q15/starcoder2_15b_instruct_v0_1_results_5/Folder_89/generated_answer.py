def sum_odd_ints_inclusive(int_list):
    sum_odd = 0
    for i, num in enumerate(int_list):
        if i >= 56 and i <= 82 and (num % 2 == 1):
            sum_odd += num
    return sum_odd