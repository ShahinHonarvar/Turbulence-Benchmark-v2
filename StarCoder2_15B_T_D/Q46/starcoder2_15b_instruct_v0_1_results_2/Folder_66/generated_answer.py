def gcf_three_nums(nums):
    n92 = nums[92]
    n69 = nums[69]
    n95 = nums[95]
    while n92 != n69:
        if n92 > n69:
            n92 -= n69
        else:
            n69 -= n92
    gcf = n92
    while n95 != gcf:
        if n95 > gcf:
            n95 -= gcf
        else:
            gcf -= n95
    return gcf