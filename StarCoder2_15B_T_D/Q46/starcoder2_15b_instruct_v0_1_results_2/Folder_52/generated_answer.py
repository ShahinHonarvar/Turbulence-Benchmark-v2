def gcf_three_nums(nums):
    num1 = nums[19]
    num2 = nums[49]
    num3 = nums[74]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_two_nums = gcf(num1, num2)
    gcf_three_nums = gcf(gcf_two_nums, num3)
    return gcf_three_nums