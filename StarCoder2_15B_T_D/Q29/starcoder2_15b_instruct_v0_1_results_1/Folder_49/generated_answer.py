def gcf_two_nums(nums):
    if len(nums) < 29:
        return None
    num1 = nums[28]
    num2 = nums[20]

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    return gcf(num1, num2)