def gcf_three_nums(nums):
    num1 = nums[92]
    num2 = nums[69]
    num3 = nums[95]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf1 = gcf(num1, num2)
    gcf_three = gcf(gcf1, num3)
    return gcf_three