def sum_even_ints_inclusive(int_list):
    if len(int_list) >= 55:
        even_ints = [num for num in int_list[50:55] if num % 2 == 0]
        return sum(even_ints)
    else:
        return 0