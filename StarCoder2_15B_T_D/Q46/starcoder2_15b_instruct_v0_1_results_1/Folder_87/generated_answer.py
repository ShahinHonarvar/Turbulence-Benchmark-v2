def gcf_three_nums(nums):
    gcf = nums[74]
    for i in range(74, 60, -1):
        for j in range(60, 28, -1):
            for k in range(28, 0, -1):
                if nums[i] % k == 0 and nums[j] % k == 0 and (gcf % k == 0):
                    gcf = k
                    break
            if gcf == 1:
                break
        if gcf == 1:
            break
    return gcf