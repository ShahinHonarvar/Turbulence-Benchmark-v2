def if_perfect_num(nums):
    if 80 < len(nums):
        return perfect_number(nums[80])
    return False

def perfect_number(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n