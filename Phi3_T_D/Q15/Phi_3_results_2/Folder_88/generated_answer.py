def sum_odd_ints_inclusive(integers):
    total_sum = sum((number for number in integers[4:9] if number % 2 != 0))
    return total_sum