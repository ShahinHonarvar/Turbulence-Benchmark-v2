def all_pos_ints_exclusive(nums):
    result = []
    for i in range(86, 89):
        if nums[i] > 0:
            result.append(nums[i])
    return result