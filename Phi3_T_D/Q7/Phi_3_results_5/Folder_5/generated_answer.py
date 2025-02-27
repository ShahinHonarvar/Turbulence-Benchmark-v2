def all_even_ints_inclusive(int_list):
    start = min(9, len(int_list))
    end = min(start + 1, len(int_list))
    return [num for num in int_list[start:end] if num % 2 == 0]