def gcf_two_nums(nums):
    num1 = nums[28]
    num2 = nums[67]

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    return gcf(num1, num2)