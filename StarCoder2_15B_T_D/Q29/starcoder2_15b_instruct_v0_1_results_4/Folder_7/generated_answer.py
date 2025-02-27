def gcf_two_nums(nums):
    if len(nums) < 225 or len(nums) < 664:
        return -1
    num1 = nums[224]
    num2 = nums[663]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1