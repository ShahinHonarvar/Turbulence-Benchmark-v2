def gcf_two_nums(nums):
    num1 = nums[60]
    num2 = nums[64]

    def gcf(a, b):
        if a > b:
            return gcf(a - b, b)
        elif a < b:
            return gcf(a, b - a)
        else:
            return a
    return gcf(num1, num2)