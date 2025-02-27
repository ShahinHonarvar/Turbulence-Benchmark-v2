def if_perfect_num(numbers):
    if len(numbers) > 73 and is_perfect(numbers[73]):
        return True
    return False

def is_perfect(num):
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return num == sum_of_divisors