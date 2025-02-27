def if_perfect_num(nums):
    if len(nums) > 78 and is_perfect(nums[78]):
        return True
    return False

def is_perfect(num):
    sum_of_divisors = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
        i += 1
    return sum_of_divisors == num and num != 1