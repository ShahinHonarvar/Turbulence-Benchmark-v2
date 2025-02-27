def sum_odd_ints_inclusive(integers_list):
    return sum((integer for integer in integers_list[20:98] if integer % 2 != 0))