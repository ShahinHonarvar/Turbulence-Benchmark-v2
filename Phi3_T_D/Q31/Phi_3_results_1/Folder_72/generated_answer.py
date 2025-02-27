def if_perfect_num(nums):
    if 16 < len(nums):
        return is_perfect_number(nums[16])
    return False

def is_perfect_number(num):
    if num < 1:
        return False
    sum_of_divisors = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
        i += 1
    return sum_of_divisors == num