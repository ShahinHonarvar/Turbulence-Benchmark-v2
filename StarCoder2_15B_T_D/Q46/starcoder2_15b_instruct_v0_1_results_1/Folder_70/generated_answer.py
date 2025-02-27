def gcf_three_nums(nums):
    gcf = nums[990]
    for n in nums[991:671:-1]:
        while n > 0:
            gcf, n = (n, gcf % n)
    for n in nums[672:711]:
        while n > 0:
            gcf, n = (n, gcf % n)
    return gcf