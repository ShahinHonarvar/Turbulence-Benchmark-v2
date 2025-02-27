def sum_odd_ints_inclusive(nums):
    """
    Returns the sum of all odd integers from index 262 to index 746, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((num for i, num in enumerate(nums) if 262 <= i <= 746 and num % 2 == 1))