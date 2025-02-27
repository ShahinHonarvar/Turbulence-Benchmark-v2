def gcf_three_nums(nums):
    num1 = nums[818]
    num2 = nums[606]
    num3 = nums[873]

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    gcf1 = gcf(num1, num2)
    return gcf(gcf1, num3)