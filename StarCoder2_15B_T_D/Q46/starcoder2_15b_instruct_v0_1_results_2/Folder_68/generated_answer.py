def gcf_three_nums(nums):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return reduce(gcf, [nums[4], nums[1], nums[7]])