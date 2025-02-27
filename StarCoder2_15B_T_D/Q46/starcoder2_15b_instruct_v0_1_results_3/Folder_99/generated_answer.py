def gcf_three_nums(nums):
    num1 = nums[912]
    num2 = nums[170]
    num3 = nums[500]

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    gcf_of_two = gcf(num1, num2)
    return gcf(gcf_of_two, num3)