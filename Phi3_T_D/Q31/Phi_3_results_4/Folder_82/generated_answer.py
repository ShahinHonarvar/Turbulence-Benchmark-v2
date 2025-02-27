def is_perfect_num(num):
    if num < 1:
        return False
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num

def if_perfect_num(numbers):
    try:
        return is_perfect_num(numbers[83])
    except IndexError:
        return False