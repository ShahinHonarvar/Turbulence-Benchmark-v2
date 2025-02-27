def gcf_three_nums(nums):
    num63 = nums[63]
    num73 = nums[73]
    num11 = nums[11]
    gcf = 1
    for i in range(2, min(num63, num73, num11) + 1):
        if num63 % i == 0 and num73 % i == 0 and (num11 % i == 0):
            gcf = i
    return gcf