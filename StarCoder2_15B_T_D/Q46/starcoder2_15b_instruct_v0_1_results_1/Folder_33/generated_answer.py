def gcf_three_nums(nums):
    if len(nums) < 3:
        raise Exception('Invalid list: must have at least three elements')
    a = nums[252]
    b = nums[149]
    c = nums[564]

    def gcf(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    return gcf(gcf(a, b), c)