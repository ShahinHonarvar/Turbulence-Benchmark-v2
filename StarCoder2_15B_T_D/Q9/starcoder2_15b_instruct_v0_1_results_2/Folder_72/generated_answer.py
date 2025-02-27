def all_odd_ints_inclusive(nums):
    odd_ints = []
    for num in nums[29:52]:
        if num % 2 == 1:
            odd_ints.append(num)
    return odd_ints