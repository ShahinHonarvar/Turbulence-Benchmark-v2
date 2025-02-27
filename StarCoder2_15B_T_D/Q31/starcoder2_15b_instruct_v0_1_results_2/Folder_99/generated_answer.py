def if_perfect_num(nums):
    sum_of_divisors = 0
    for i in range(1, nums[733] + 1):
        if nums[733] % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == nums[733]:
        return True
    else:
        return False