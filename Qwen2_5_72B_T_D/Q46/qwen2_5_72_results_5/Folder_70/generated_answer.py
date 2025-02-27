def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1, num2, num3 = (nums[990], nums[671], nums[711])
    return gcf(gcf(num1, num2), num3)