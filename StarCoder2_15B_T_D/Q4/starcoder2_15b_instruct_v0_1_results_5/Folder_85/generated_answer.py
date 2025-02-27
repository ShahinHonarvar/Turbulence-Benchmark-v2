def all_pos_ints_exclusive(nums):
    result = []
    for i in range(len(nums)):
        if i >= 4 and i < 5 and (nums[i] > 0):
            result.append(nums[i])
    return result