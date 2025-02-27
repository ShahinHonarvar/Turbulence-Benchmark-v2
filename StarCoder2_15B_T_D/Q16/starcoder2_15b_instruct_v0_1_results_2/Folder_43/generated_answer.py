def sum_even_ints_inclusive(ints):
    start_index = 68
    end_index = 86
    sum_even_ints = 0
    for i, num in enumerate(ints):
        if i >= start_index and i <= end_index:
            if num % 2 == 0:
                sum_even_ints += num
    return sum_even_ints