def if_perfect_num(nums):
    if len(nums) > 92:
        sum_of_divisors = sum((i for i in range(1, nums[92]) if nums[92] % i == 0))
        return sum_of_divisors == nums[92]
    return False