def all_even_ints_exclusive(lst):
    """
    Write a function called 'all_even_ints_exclusive' that takes one argument, a list of integers, and returns the list of all even integers from index 66 to index 90, both exclusive. If no even integers exist in the specified range, the function should return an empty list.
    """
    even_ints = []
    for i in range(66, 90):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints