def sum_even_ints_inclusive(int_list):
    filtered_list = [num for num in int_list[17:79] if num % 2 == 0]
    return sum(filtered_list) if filtered_list else 0