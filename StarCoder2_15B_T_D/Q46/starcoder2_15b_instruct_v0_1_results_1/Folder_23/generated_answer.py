def gcf_three_nums(nums):
    num_31 = nums[31]
    num_25 = nums[25]
    num_80 = nums[80]
    gcf = num_31
    while gcf != num_25 and gcf != num_80:
        if gcf > num_25 and gcf > num_80:
            gcf -= 1
        elif gcf < num_25 and gcf < num_80:
            gcf += 1
    return gcf