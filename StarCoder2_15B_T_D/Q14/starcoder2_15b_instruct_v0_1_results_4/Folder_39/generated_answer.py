def find_second_smallest_num(nums):
    """
    Finds the second smallest element from index 28 to 40, both inclusive.
    If there is no such an element, returns None.
    """
    second_smallest = None
    for i in range(28, 41):
        if nums[i] < nums[i + 1]:
            second_smallest = nums[i + 1]
            break
    return second_smallest