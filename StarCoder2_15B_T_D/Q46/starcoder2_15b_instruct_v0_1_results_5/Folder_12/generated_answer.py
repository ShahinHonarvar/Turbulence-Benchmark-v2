def gcf_three_nums(nums):
    num_91 = nums[91]
    num_45 = nums[45]
    num_48 = nums[48]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num_91, num_45), num_48)