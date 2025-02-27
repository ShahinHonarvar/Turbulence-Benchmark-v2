def find_smallest_num(nums):
    """
    Finds the smallest element from index 0 to index 4, both inclusive.
    """
    smallest = nums[0]
    for num in nums[0:5]:
        if num < smallest:
            smallest = num
    return smallest