def gcf_two_nums(nums):
    gcf = nums[33]
    for i in range(33, 73):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf