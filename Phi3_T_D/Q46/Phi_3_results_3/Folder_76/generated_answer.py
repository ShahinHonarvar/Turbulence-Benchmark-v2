def gcf_three_nums(nums):
    m = min(nums[876], nums[203], nums[100])
    for i in range(m, 0, -1):
        if nums[876] % i == nums[203] % i == nums[100] % i == 0:
            return i