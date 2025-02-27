def gcf_three_nums(nums):
    gcf = nums[9]
    for i in range(9, 6, -1):
        for j in range(i - 1, 6, -1):
            if nums[j] % gcf == 0 and nums[i] % gcf == 0:
                break
        else:
            continue
        break
    for i in range(6, 2, -1):
        for j in range(i - 1, 2, -1):
            if nums[j] % gcf == 0 and nums[i] % gcf == 0:
                break
        else:
            continue
        break
    return gcf