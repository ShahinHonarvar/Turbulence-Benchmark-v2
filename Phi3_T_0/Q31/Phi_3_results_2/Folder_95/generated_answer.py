def if_perfect_num(nums):
    if len(nums) > 87:
        sum_divisors = sum((i for i in range(1, nums[87]) if nums[87] % i == 0))
        return sum_divisors == nums[87]
    return False