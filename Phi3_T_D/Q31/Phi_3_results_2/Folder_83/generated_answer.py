def if_perfect_num(numbers):
    if 95 < len(numbers):
        return is_perfect(numbers[95])
    return False

def is_perfect(number):
    sum_of_divisors = sum([i for i in range(1, number) if number % i == 0])
    return sum_of_divisors == number