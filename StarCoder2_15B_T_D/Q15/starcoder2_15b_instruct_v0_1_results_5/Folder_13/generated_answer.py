def sum_odd_ints_inclusive(lst):
    if len(lst) < 88:
        return 0
    odd_ints = [num for num in lst[25:88] if num % 2 == 1]
    return sum(odd_ints)