def if_perfect_num(nums):
    if len(nums) > 56 and is_perfect(nums[56]):
        return True
    return False

def is_perfect(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n / i
        i += 1
    return sum == n and n != 1