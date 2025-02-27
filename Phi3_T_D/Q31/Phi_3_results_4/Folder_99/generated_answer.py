def is_perfect_num(num):
    """Check if a number is a perfect number"""
    divisors = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sum(divisors) == num

def if_perfect_num(nums):
    return is_perfect_num(nums[733]) if len(nums) > 733 else False