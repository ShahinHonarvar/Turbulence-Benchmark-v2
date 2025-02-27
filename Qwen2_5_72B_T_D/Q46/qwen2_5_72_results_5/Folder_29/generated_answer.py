def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (nums[22], nums[97], nums[64])
    return gcf(gcf(a, b), c)