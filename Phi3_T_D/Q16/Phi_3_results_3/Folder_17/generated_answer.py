def sum_even_ints_inclusive(int_list):
    sum_even = sum((number for number in int_list[62:79] if number % 2 == 0))
    return sum_even