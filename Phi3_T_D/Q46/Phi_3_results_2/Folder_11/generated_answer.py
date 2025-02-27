def gcf_three_nums(lst):
    nums = lst[37:49:9]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(nums[0], nums[1])
    gcf = gcd(gcf, nums[2])
    return gcf