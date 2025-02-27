from the given list of integers. If no even integers exist in the specified range,

def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 37 to index 51, both inclusive,
    an empty list is returned.
    """
    return [n for i, n in enumerate(nums) if i >= 37 and i <= 51 and (n % 2 == 0)]