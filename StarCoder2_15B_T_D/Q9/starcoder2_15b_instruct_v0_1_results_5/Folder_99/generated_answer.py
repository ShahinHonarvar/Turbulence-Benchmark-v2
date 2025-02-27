from the given list of integers. If no odd integers exist in the specified range,

def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 310 to index 370, both inclusive,
    an empty list is returned.
    """
    odd_ints = []
    for i, num in enumerate(nums):
        if i >= 310 and i <= 370 and (num % 2 != 0):
            odd_ints.append(num)
    return odd_ints