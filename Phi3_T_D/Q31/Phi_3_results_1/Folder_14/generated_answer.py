def is_perfect_num(num):
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num

def if_perfect_num(nums):
    return is_perfect_num(nums[17]) if len(nums) > 17 else False