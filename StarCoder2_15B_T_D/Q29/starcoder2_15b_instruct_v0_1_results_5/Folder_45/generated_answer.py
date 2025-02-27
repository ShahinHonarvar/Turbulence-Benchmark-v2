def gcf_two_nums(nums):
    gcf = nums[47]
    for i in range(48, 98):
        gcf = gcf_two_nums_helper(gcf, nums[i])
    return gcf

def gcf_two_nums_helper(num1, num2):
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1