def sum_odd_ints_inclusive(integers):
    total_sum = sum((num for num in integers[40:81] if num % 2 != 0))
    return total_sum