def if_perfect_num(nums):
    divisors_sum = 0
    for i in range(1, nums[10]):
        if nums[10] % i == 0:
            divisors_sum += i
    return divisors_sum == nums[10]