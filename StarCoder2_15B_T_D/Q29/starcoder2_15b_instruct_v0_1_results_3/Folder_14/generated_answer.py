def gcf_two_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_result = gcf(nums[49], nums[53])
    return gcf_result