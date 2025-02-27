def sum_odd_ints_inclusive(integers):
    return sum((number for number in integers[1:2] if number % 2 != 0))