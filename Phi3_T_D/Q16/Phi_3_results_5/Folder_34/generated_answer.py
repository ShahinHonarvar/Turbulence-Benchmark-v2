def sum_even_ints_inclusive(integers):
    result = sum((int(i) for i in integers[60:201] if i % 2 == 0))
    return result