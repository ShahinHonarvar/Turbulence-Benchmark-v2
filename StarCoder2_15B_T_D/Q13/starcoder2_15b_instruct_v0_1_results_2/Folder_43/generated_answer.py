def find_second_largest_num(nums):
    """
    Finds the second largest element from index 68 to index 86, both inclusive.
    If there is no such element, returns 'None'.
    """
    sublist = nums[68:87]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]