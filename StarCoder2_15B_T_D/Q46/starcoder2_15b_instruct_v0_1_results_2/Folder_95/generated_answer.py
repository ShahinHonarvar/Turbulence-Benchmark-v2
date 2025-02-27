def gcf_three_nums(nums):
    gcf = nums[87]
    for i in range(86, 19, -1):
        if nums[i] == 0:
            continue
        while nums[i] % gcf != 0:
            gcf -= 1
        if gcf == 1:
            break
    return gcf