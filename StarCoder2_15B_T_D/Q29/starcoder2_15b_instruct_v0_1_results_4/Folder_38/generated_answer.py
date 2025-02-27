def gcf_two_nums(nums):
    n88 = nums[88]
    n35 = nums[35]
    while n35 != 0:
        n88, n35 = (n35, n88 % n35)
    return n88