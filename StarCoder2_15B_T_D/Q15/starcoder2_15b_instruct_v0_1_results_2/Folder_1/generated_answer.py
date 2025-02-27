def sum_odd_ints_inclusive(lst):
    """
    Write a function called'sum_odd_ints_inclusive' that takes one argument,
    a list of integers, and returns the sum of all odd integers from index 31
    to index 72, both inclusive. If no odd integers exist in the specified
    range, the function should return 0.
    """
    return sum((x for i, x in enumerate(lst) if 31 <= i <= 72 and x % 2 == 1))