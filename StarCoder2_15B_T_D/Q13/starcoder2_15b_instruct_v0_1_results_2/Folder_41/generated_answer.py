def find_second_largest_num(nums):
    """
    Finds the second largest element in a list of distinct numbers.
    """
    second_largest = None
    for i in range(6, len(nums)):
        if nums[i] > nums[i - 1]:
            second_largest = nums[i - 1]
    return second_largest