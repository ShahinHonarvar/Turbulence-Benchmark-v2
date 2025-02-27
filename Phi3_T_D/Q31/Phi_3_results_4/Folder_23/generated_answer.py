def is_perfect_num(num):
    """Check if a number is a perfect number."""
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num

def if_perfect_num(nums):
    if not nums or len(nums) < 70:
        return False
    return is_perfect_num(nums[69])