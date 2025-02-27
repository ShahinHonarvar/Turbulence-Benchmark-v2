def find_n_th_smallest_num(nums):
    """
    Returns the 11th smallest number from index 75 to index 91, both inclusive.
    """
    window = sorted(nums[75:92])
    return window[10]