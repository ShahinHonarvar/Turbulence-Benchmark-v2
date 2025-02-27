def if_perfect_num(numbers):
    if len(numbers) >= 20:
        return is_perfect(numbers[19])
    else:
        return False

def is_perfect(number):
    sum_divisors = sum((div for div in range(1, number // 2 + 1) if number % div == 0))
    return sum_divisors == number