def find_n_th_smallest_num(nums):
    if not isinstance(nums, list) or len(nums[39:92]) < 17:
        return None
    return sorted(nums[39:92])[16]