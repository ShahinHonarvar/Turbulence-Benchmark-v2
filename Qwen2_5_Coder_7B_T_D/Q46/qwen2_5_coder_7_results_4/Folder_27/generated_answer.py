def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    n1, n2, n3 = (nums[76], nums[64], nums[28])
    return gcf(gcf(n1, n2), n3)