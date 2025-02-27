def gcf_three_nums(nums):
    n96 = nums[96]
    n53 = nums[53]
    n35 = nums[35]
    a = min(n96, n53, n35)
    b = max(n96, n53, n35)
    r = b % a
    while r != 0:
        b = a
        a = r
        r = b % a
    return a