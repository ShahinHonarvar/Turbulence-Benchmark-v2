def find_second_smallest_num(nums):
    """
    Finds the second smallest element from index 31 to index 72, both inclusive.
    If there is no such an element, returns 'None'.
    """
    second_smallest = None
    for i in range(31, 73):
        if second_smallest is None or nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest