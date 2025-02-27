def gcf_three_nums(nums):
    gcf = nums[1]
    for i in range(2, 8):
        if i == 7:
            gcf = nums[i]
        else:
            while gcf != nums[i]:
                if gcf > nums[i]:
                    gcf -= nums[i]
                else:
                    nums[i] -= gcf
    return gcf