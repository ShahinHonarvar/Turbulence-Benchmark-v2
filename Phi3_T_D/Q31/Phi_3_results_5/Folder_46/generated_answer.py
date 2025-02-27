def is_perfect_num(num):
    return num == sum([i for i in range(1, num) if num % i == 0])

def if_perfect_num(nums):
    return is_perfect_num(nums[453]) if len(nums) > 453 else False