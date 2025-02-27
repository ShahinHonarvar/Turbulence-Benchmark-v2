def sum_odd_ints_inclusive(integers):
    return sum((integer for integer in integers[75:95] if integer % 2 != 0))