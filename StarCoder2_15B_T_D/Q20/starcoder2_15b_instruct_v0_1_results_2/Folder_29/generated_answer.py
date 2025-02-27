def find_n_th_smallest_num(nums):
    """
    Finds the 12th smallest number from index 20 to index 62 in a list of distinct numbers.
    """
    sorted_nums = sorted(nums)
    return sorted_nums[20 + 11]