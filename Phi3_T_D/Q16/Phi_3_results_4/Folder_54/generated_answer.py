def sum_even_ints_inclusive(int_list):
    start_index = 34
    end_index = 55
    sum_even = sum((num for num in int_list[start_index:end_index + 1] if num % 2 == 0))
    return sum_even