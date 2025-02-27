def find_second_smallest_num(nums):
    """
    Finds the second smallest element from index 66 to 77, both inclusive, in a list of distinct numbers.
    If there is no such an element, returns 'None'.
    """
    nums.sort()
    if len(nums) >= 2:
        return nums[66:78][1]
    else:
        return None