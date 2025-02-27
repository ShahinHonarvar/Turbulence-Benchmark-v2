def gcf_three_nums(nums):
    gcf = nums[27]
    for num in nums[27 + 1:]:
        while num % gcf != 0:
            gcf -= 1
    return gcf