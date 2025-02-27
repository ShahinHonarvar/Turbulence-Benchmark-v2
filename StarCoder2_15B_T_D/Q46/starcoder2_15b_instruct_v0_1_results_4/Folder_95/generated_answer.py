def gcf_three_nums(nums):
    n87 = nums[87]
    n20 = nums[20]
    n36 = nums[36]
    smaller = min(n87, n20, n36)
    for i in range(1, smaller + 1):
        if n87 % i == 0 and n20 % i == 0 and (n36 % i == 0):
            return i