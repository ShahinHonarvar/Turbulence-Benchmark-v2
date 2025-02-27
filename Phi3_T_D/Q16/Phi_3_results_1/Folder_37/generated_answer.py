def sum_even_ints_inclusive(integers):
    return sum((number for number in integers[1:6] if number % 2 == 0))