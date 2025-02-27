def is_perfect_num(num):
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_of_divisors == num

def if_perfect_num(nums):
    if len(nums) > 87 and is_perfect_num(nums[87]):
        return True
    return False