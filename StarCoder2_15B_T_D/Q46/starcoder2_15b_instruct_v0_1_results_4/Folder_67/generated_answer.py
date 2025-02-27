def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a = nums[70]
    b = nums[41]
    c = nums[20]
    return gcf(gcf(a, b), c)