def sum_even_ints_inclusive(integers):
    even_sum = sum((integer for integer in integers[90:100] if integer % 2 == 0))
    return even_sum