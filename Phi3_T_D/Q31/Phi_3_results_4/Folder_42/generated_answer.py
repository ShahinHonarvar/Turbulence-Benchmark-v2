def if_perfect_num(nums):
    perfect = [1] if nums[276] == 1 else []
    for i in range(1, nums[276] // 2 + 1):
        if nums[276] % i == 0:
            perfect.append(i)
    return nums[276] == sum(perfect)