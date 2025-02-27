def if_perfect_num(nums):
    if len(nums) > 95:
        temp_num = nums[95]
        divisors = [i for i in range(1, temp_num // 2 + 1) if temp_num % i == 0]
        return sum(divisors) == temp_num
    return False