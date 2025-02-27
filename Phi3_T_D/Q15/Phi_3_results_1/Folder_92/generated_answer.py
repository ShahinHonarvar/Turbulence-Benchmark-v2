def sum_odd_ints_inclusive(lt):
    total = sum((value for value in lt[1:2] if value % 2 != 0))
    return total