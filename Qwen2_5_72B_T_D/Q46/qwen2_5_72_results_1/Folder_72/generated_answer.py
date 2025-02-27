def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (nums[44], nums[91], nums[42])
    return gcf(gcf(a, b), c)