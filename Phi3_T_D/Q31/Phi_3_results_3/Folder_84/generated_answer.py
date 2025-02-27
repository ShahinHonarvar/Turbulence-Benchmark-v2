def if_perfect_num(nums):
    if len(nums) > 685 and is_perfect_num(nums[685]):
        return True
    return False

def is_perfect_num(n):
    sum_of_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                sum_of_divisors += n // i
    return sum_of_divisors == n