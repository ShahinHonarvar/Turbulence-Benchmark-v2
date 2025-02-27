def sum_even_ints_inclusive(numbers_list):
    start_index, end_index = (32, 35)
    sum_even = sum((num for num in numbers_list[start_index:end_index + 1] if num % 2 == 0))
    return sum_even