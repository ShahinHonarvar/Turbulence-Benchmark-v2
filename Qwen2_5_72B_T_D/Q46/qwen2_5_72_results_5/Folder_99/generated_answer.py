def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (nums[912], nums[170], nums[500])
    return gcf(gcf(a, b), c)