def find_largest_num(nums):
    """
    Find the largest element from index 50 to index 200, both inclusive, in a list of numbers.
    """
    sliced_list = nums[50:201]
    largest = max(sliced_list)
    return largest