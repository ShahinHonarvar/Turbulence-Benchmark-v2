def gcf_three_nums(nums):
    a = nums[70]
    b = nums[98]
    c = nums[22]
    min_num = min(a, b, c)
    for i in range(min_num, 0, -1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i