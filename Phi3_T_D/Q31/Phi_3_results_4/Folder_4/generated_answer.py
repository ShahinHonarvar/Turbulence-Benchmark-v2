def is_perfect(number):
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == number

def if_perfect_num(numbers):
    if 15 < len(numbers):
        return is_perfect(numbers[15])
    return False