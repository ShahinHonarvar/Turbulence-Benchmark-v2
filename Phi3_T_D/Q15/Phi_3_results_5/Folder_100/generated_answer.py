def sum_odd_ints_inclusive(integers):
    odd_sum = sum((int(odd) for odd in integers[42:69] if int(odd) % 2 != 0))
    return odd_sum