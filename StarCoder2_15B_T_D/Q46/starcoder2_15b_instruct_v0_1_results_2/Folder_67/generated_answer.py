def gcf_three_nums(nums):
    gcf = nums[70]
    for i in range(70, 40, -1):
        for j in range(40, 20, -1):
            for k in range(20, 0, -1):
                if nums[i] % k == 0 and nums[j] % k == 0 and (gcf % k == 0):
                    gcf = k
                    break
            if gcf == 1:
                break
        if gcf == 1:
            break
    return gcf