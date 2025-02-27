def if_perfect_num(numbers):
    if 194 < len(numbers) and is_perfect_number(numbers[194]):
        return True
    else:
        return False

def is_perfect_number(num):
    if num <= 1:
        return False
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors == num