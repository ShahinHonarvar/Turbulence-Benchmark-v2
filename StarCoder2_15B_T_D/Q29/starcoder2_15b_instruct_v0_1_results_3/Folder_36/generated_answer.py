def gcf_two_nums(nums):

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    return gcf(nums[429], nums[289])