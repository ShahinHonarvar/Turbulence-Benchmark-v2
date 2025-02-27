def find_second_smallest_num(nums):
    """
    Finds the second smallest element from index 262 to index 746, both inclusive.
    If there is no such an element, returns 'None'.
    """
    nums.sort()
    if len(nums[262:747]) >= 2:
        return nums[262:747][1]
    else:
        return None