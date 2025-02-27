def sum_even_ints_inclusive(lst):
    start, end = (17, 78)
    return sum((num for num in lst[start:end + 1] if num % 2 == 0))