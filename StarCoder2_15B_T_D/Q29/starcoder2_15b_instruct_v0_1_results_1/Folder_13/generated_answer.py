def gcf_two_nums(nums):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(nums[534], nums[630])