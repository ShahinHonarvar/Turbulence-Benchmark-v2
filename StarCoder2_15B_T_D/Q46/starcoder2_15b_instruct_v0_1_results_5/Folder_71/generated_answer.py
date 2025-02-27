def gcf_three_nums(nums):
    num24 = nums[24]
    num45 = nums[45]
    num38 = nums[38]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    gcf24_45 = gcf(num24, num45)
    return gcf(gcf24_45, num38)