def sum_even_ints_inclusive(int_list):
    even_ints = [num for num in int_list[50:55] if num % 2 == 0]
    return sum(even_ints) if even_ints else 0