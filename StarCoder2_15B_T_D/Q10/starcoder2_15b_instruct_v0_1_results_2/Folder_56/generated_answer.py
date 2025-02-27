def all_odd_ints_exclusive(nums):
    odd_ints = []
    for i in range(7, 9):
        if nums[i] % 2 == 1:
            odd_ints.append(nums[i])
    return odd_ints