def gcf_two_nums(nums):
    num1 = nums[198]
    num2 = nums[212]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(num1, num2)