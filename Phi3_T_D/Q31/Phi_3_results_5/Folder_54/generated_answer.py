def is_perfect_num(numbers):
    if len(numbers) <= 51:
        return False
    return sum_of_divisors(numbers[51]) == numbers[51]

def sum_of_divisors(num):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    return sum_div