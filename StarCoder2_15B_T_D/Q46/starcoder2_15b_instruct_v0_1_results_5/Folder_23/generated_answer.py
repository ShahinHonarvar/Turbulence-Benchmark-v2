def gcf_three_nums(nums):
    gcf = nums[31]
    for i in range(31, 81):
        if nums[i] < gcf:
            gcf = nums[i]
    for i in range(31, 81):
        if nums[i] % gcf != 0:
            for j in range(2, min(nums[i], gcf) + 1):
                if nums[i] % j == 0 and gcf % j == 0:
                    gcf //= j
                    break
    return gcf