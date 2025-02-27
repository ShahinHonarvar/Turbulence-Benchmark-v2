def sum_odd_ints_inclusive(lst):
    start, end = (70, 200)
    return sum((element for element in lst[start:end + 1] if element % 2 != 0))