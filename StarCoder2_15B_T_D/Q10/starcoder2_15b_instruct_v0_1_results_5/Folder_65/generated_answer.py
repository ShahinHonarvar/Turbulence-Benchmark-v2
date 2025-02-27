def all_odd_ints_exclusive(nums):
    result = []
    for i in range(42, 87):
        if i % 2 == 1:
            result.append(nums[i])
    return result