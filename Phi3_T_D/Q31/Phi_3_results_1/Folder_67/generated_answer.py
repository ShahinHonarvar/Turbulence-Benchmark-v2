def if_perfect_num(nums):
    if len(nums) > 43 and is_perfect(nums[43]):
        return True
    return False

def is_perfect(number):
    sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum += divisor
    return sum == number