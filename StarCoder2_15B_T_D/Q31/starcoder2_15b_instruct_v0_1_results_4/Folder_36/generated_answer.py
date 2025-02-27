def if_perfect_num(nums):
    if nums[990] > 0:
        sum_of_divisors = 0
        for i in range(1, nums[990]):
            if nums[990] % i == 0:
                sum_of_divisors += i
        if sum_of_divisors == nums[990]:
            return True
    return False