def find_n_th_smallest_num(nums):
    """
    Finds the 18th smallest number from index 56 to index 96, both inclusive.
    """
    sorted_nums = sorted(nums[56:97])
    return sorted_nums[17]