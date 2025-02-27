def gcf_two_nums(nums):
    if len(nums) < 2:
        return None
    num1, num2 = (nums[1], nums[2])
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1