def find_second_smallest_num(nums):
    """
    Finds the second smallest element in `nums` between index 56 and index 82, both inclusive.
    If there is no such an element, returns `None`.
    """
    second_smallest = None
    for i in range(56, 83):
        if nums[i] < nums[i + 1]:
            second_smallest = nums[i + 1]
            break
    return second_smallest