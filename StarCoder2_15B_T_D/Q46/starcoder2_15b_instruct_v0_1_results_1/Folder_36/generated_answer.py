def gcf_three_nums(nums):
    gcf = nums[427]
    for i in [761, 148]:
        while nums[i] % gcf != 0:
            gcf = nums[i] % gcf
    return gcf