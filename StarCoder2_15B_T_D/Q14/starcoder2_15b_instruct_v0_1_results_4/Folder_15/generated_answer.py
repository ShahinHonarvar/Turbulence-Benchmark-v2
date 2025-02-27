def find_second_smallest_num(nums):
    """
    Finds the second smallest element from index 0 to index 3, both inclusive.
    If there is no such an element, returns 'None'.
    """
    if len(nums) < 2:
        return None
    smallest = nums[0]
    second_smallest = None
    for num in nums[1:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest