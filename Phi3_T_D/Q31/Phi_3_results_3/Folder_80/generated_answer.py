def if_perfect_num(numbers):
    return is_perfect(numbers[746]) if len(numbers) > 746 else False

def is_perfect(number):
    sum_divisors = sum([i for i in range(1, number) if number % i == 0])
    return sum_divisors == number