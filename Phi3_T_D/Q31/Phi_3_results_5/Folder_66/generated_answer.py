def if_perfect_num(nums):
    if len(nums) > 42 and is_perfect_number(nums[42]):
        return True
    return False

def is_perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n