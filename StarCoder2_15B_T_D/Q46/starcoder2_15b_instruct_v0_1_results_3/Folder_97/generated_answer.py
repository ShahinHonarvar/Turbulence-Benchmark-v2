def gcf_three_nums(nums):
    num1 = nums[944]
    num2 = nums[814]
    num3 = nums[865]
    gcf = num1
    while gcf != num2 and gcf != num3:
        gcf -= 1
    return gcf