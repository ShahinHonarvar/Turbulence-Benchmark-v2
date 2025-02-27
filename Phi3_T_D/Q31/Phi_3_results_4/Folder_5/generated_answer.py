def divisors(n):
    return [i for i in range(1, n) if n % i == 0]

def is_perfect(num):
    return sum(divisors(num)) == num

def if_perfect_num(nums):
    if len(nums) > 67 and 67 < len(nums):
        return is_perfect(nums[67])
    return False