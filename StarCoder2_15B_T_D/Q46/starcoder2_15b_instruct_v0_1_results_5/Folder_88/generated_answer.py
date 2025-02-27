def gcf_three_nums(nums):
    a = nums[47]
    b = nums[10]
    c = nums[28]

    def gcf(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    return gcf(gcf(a, b), c)