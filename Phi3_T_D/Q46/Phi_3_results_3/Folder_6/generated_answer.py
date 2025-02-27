def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    idx_93, idx_94, idx_57 = (93, 94, 57)
    num93 = nums[idx_93] if idx_93 < len(nums) else 0
    num94 = nums[idx_94] if idx_94 < len(nums) else 0
    num57 = nums[idx_57] if idx_57 < len(nums) else 0
    temp_gcf = gcd(num93, num94)
    return gcd(temp_gcf, num57)