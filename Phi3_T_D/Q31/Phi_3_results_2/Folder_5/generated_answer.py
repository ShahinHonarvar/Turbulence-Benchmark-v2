def if_perfect_num(nums):
    if len(nums) > 67:
        original_num = nums[67]
        divisors = [i for i in range(1, original_num) if original_num % i == 0]
        return sum(divisors) == original_num
    return False