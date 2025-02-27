def sum_even_ints_inclusive(lst):
    if len(lst) < 112:
        return 0
    return sum((num for num in lst[111:112] if num % 2 == 0))