def is_valid_divisor(num):
    return num >= 2 and num <= 4 and (num != 0)

def sum_of_divisors_in_range(num):
    sum_of_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0 and is_valid_divisor(i):
            sum_of_divisors += i
    return sum_of_divisors