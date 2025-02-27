def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 0 to index 5, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    result = []
    for num in nums:
        if num % 2 != 0 and 0 <= nums.index(num) <= 5:
            result.append(num)
    return result