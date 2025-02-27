def gcf_three_nums(nums):
    num1 = nums[24]
    num2 = nums[45]
    num3 = nums[38]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    gcf_12 = gcf(num1, num2)
    return gcf(gcf_12, num3)