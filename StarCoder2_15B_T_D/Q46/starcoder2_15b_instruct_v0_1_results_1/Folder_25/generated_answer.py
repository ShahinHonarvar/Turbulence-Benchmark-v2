def gcf_three_nums(nums):
    gcf = nums[32]
    for i in range(32, 55):
        for j in range(i + 1, 55):
            if nums[i] % nums[j] == 0:
                gcf = nums[j]
                break
        for k in range(j + 1, 55):
            if nums[j] % nums[k] == 0:
                gcf = nums[k]
                break
    return gcf