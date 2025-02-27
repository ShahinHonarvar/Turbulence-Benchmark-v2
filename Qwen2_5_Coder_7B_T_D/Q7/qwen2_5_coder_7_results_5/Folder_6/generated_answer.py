def all_even_ints_inclusive(lst):
    return [num for i, num in enumerate(lst, start=1) if 10 <= i <= 66 and num % 2 == 0]