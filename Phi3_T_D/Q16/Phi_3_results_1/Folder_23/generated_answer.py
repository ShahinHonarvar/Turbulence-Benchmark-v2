def sum_even_ints_inclusive(int_list):
    start_index = 52
    end_index = 71
    sum_even = sum((num for num in int_list[start_index:end_index + 1] if num % 2 == 0))
    return sum_even