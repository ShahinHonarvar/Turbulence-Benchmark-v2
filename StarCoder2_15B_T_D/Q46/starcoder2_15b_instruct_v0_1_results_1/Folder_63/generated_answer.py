def gcf_three_nums(nums):
    num1 = nums[38]
    num2 = nums[52]
    num3 = nums[69]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_two_nums = gcf(num1, num2)
    return gcf(gcf_two_nums, num3)