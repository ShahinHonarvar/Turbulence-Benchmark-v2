def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (nums[56], nums[54], nums[13])
    return gcf(gcf(a, b), c)