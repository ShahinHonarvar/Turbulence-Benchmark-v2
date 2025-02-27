def sum_even_ints_inclusive(lst):
    running_sum = 0
    for num in lst:
        if num % 2 == 0:
            running_sum += num
    return running_sum