def all_pos_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if i >= 0 and i <= 2:
            if nums[i] > 0:
                result.append(nums[i])
    return result