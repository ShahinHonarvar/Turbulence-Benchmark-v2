def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    idx1, idx2, idx3 = (818, 606, 873)
    gcd_12 = gcd(nums[min(idx1, idx2)], nums[max(idx1, idx2)])
    return gcd(gcd_12, nums[idx3])