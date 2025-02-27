def gcf_two_nums(nums):
    n1 = nums[78]
    n2 = nums[93]
    if n1 > n2:
        smaller = n2
    else:
        smaller = n1
    for i in range(1, smaller + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcf = i
    return gcf