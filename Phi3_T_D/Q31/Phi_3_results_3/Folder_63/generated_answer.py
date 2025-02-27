def if_perfect_num(numbers):
    return is_perfect(numbers[57]) if len(numbers) > 57 else False

def is_perfect(num):
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return num == sum_of_divisors