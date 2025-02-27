def all_even_ints_inclusive(lst):
    """
    Write a function called 'all_even_ints_inclusive' that takes one argument, a list of integers,
    and returns the list of all even integers from index 19 to index 92, both inclusive. If no
    even integers exist in the specified range, the function should return an empty list.
    """
    if len(lst) < 93:
        return []
    return [x for x in lst[19:93] if x % 2 == 0]