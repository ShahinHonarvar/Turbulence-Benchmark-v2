def sum_even_ints_inclusive(integers):
    return sum((integer for integer in integers[37:77])) if sum((integer for integer in integers[37:77] if integer % 2 == 0)) > 0 else 0