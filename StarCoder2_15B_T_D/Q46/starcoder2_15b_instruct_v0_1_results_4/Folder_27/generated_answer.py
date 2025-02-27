def gcf_three_nums(nums):
    num_76 = nums[76]
    num_64 = nums[64]
    num_28 = nums[28]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_64_76 = gcf(num_64, num_76)
    return gcf(gcf_64_76, num_28)