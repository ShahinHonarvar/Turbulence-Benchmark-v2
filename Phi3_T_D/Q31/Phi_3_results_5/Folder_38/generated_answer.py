def if_perfect_num(nums):
    if len(nums) > 38 and is_perfect(nums[38]):
        return True
    return False

def is_perfect(num):
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return num == sum_divisors