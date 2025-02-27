def sum_even_ints_inclusive(int_list):
    even_sum = sum((number for number in int_list[55:99] if number % 2 == 0))
    return even_sum if even_sum else 0