def is_perfect_num(num):
    return num == sum((i for i in range(1, num) if num % i == 0))

def if_perfect_num(nums):
    return is_perfect_num(nums[27]) if len(nums) > 27 else False