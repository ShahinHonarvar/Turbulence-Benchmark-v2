def if_perfect_num(numbers):
    if len(numbers) > 77 and is_perfect(numbers[77]):
        return True
    return False

def is_perfect(number):
    sum_of_divisors = sum([i for i in range(1, number) if number % i == 0])
    return sum_of_divisors == number