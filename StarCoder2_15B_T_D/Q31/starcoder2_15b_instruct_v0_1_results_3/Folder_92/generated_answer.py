def if_perfect_num(nums):
    if len(nums) == 0:
        return False
    total = 0
    for i in range(1, int(nums[0] ** 0.5) + 1):
        if nums[0] % i == 0:
            total += i
            if i != 1 and i != nums[0] // i:
                total += nums[0] // i
    return total == nums[0]