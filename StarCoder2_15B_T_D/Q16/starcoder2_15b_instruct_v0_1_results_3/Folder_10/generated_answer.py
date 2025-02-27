def sum_even_ints_inclusive(lst):
    if not lst or len(lst) < 60:
        return 0
    even_ints = [num for num in lst[25:60] if num % 2 == 0]
    return sum(even_ints)