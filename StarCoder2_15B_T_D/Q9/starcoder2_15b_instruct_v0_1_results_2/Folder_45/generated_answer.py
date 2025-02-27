from a given list of integers. If no odd integers exist in the specified range,

def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 30 to index 200, both inclusive,
    the function returns an empty list.
    """
    odd_ints = []
    for i in range(30, 201):
        if numbers[i] % 2 == 1:
            odd_ints.append(numbers[i])
    return odd_ints