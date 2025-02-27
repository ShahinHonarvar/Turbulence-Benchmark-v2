def gcf_two_nums(nums):
    gcf = nums[224]
    for i in range(224, 663):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf