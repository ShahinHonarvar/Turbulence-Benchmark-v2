def all_odd_ints_inclusive(nums):
    odd_ints = []
    for i in range(6, 9):
        if nums[i] % 2 != 0:
            odd_ints.append(nums[i])
    return odd_ints