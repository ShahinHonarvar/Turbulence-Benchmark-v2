def gcf_three_nums(nums):

    def find_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return find_gcf(find_gcf(nums[9], nums[6]), nums[2])