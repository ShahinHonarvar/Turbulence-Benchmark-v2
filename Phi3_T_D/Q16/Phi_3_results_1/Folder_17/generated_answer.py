def sum_even_ints_inclusive(integers):
    total = sum((number for number in integers[62:79] if number % 2 == 0))
    return total