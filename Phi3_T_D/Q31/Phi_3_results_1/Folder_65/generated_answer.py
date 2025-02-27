def is_perfect(num):
    return num == sum((i for i in range(1, num) if num % i == 0))

def if_perfect_num(nums):
    return is_perfect(nums[35]) if len(nums) > 35 else False