def gcf_three_nums(nums):
    a, b, c = (nums[41], nums[69], nums[28])

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(a, b), c)