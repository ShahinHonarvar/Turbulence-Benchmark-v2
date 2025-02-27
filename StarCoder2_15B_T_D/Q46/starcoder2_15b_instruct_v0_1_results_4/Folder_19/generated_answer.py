def gcf_three_nums(nums):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(nums[40], gcf(nums[15], nums[99]))