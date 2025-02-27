def gcf_two_nums(nums):
    num1 = nums[0]
    num2 = nums[9]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(num1, num2)