def is_perfect_number(n):
    if n <= 1:
        return False
    sum_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n

def if_perfect_num(numbers):
    try:
        return is_perfect_number(numbers[100])
    except IndexError:
        return False