def gcf_three_nums(nums):
    num1 = nums[19]
    num2 = nums[94]
    num3 = nums[78]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_num1_num2 = gcf(num1, num2)
    gcf_num3 = gcf(gcf_num1_num2, num3)
    return gcf_num3