def all_even_ints_inclusive(nums):
    """
    Takes a list of integers and returns the list of all even integers from index 64 to index 66, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i in range(64, 67):
        if nums[i] % 2 == 0:
            even_ints.append(nums[i])
    return even_ints