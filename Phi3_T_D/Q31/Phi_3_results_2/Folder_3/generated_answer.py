def if_perfect_num(nums):
    if 100 < len(nums) and is_perfect(nums[100]):
        return True
    return False

def is_perfect(n):
    return sum((i for i in range(1, n) if n % i == 0)) == n