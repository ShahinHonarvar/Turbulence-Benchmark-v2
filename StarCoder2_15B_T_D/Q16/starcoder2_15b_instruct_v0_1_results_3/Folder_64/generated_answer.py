def sum_even_ints_inclusive(nums):
    if not nums:
        return 0
    result = 0
    for i in range(min(5, len(nums))):
        if nums[i] % 2 == 0:
            result += nums[i]
    return result