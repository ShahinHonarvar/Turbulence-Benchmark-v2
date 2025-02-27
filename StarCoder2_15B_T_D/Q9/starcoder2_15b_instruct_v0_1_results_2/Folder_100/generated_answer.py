def all_odd_ints_inclusive(nums):
    odd_ints = []
    for i in range(len(nums)):
        if i >= 42 and i <= 68 and (nums[i] % 2 == 1):
            odd_ints.append(nums[i])
    return odd_ints