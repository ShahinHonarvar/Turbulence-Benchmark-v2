def all_pos_ints_exclusive(nums):
    if not isinstance(nums, list):
        return []
    pos_ints = []
    for i in range(4, len(nums) - 1):
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints