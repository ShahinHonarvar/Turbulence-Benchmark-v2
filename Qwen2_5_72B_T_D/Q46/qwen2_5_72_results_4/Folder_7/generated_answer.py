def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(nums[477], nums[696]), nums[663])