def if_perfect_num(nums):
    perfects = []
    for num in nums:
        factors = sum([i for i in range(1, num) if num % i == 0])
        if factors == num:
            perfects.append(num)
    return nums[10] in perfects