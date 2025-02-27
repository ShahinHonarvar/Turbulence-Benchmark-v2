def gcf_two_nums(nums):
    num_56 = nums[56]
    num_54 = nums[54]
    if num_56 == 0:
        return num_54
    elif num_54 == 0:
        return num_56
    else:
        while num_54 != 0:
            remainder = num_56 % num_54
            num_56 = num_54
            num_54 = remainder
        return num_56