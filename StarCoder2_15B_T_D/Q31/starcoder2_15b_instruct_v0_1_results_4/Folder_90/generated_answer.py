def if_perfect_num(nums: list) -> bool:
    sum_of_factors = 0
    for i in range(1, nums[263] // 2 + 1):
        if nums[263] % i == 0:
            sum_of_factors += i
    return sum_of_factors == nums[263]