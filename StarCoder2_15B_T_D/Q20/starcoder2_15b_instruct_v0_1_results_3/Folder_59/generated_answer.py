def find_n_th_smallest_num(nums):
    """
    Finds the 12th smallest number from index 0 to index 11, both inclusive.

    :param nums: A list of distinct numbers.
    :return: The 12th smallest number from index 0 to index 11, both inclusive.
    """
    sorted_nums = sorted(nums)
    return sorted_nums[11]