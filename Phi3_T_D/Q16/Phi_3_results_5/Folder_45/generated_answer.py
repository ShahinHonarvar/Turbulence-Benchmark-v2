def sum_even_ints_inclusive(integers):
    return sum((integer for integer in integers[30:201] if integer % 2 == 0))