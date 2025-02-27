from the given list of integers. If no odd integers exist in the specified range,

def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 31 to index 34, both inclusive,
    an empty list is returned.
    """
    odd_ints = []
    for i, num in enumerate(numbers):
        if i >= 31 and i <= 34 and (num % 2 != 0):
            odd_ints.append(num)
    return odd_ints