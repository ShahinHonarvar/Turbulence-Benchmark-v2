def if_perfect_num(numbers):
    if len(numbers) > 21 and is_perfect(numbers[21]):
        return True
    return False

def is_perfect(num):
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors == num