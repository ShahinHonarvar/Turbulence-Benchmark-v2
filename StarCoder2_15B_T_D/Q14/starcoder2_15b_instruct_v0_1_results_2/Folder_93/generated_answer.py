def find_second_smallest_num(nums):
    """
    Finds the second smallest element from index 75 to index 88, both inclusive,
    or 'None' if there is no such an element.
    """
    second_smallest = None
    for i in range(75, 90):
        if second_smallest is None or nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest