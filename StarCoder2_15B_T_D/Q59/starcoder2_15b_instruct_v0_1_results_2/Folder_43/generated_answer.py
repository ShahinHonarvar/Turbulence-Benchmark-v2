def all_left_truncatable_prime(x):
    numbers = list(x)
    numbers.sort()
    left_truncatable_primes = []
    for number in numbers[89:]:
        if is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_left_truncatable_prime(number):
    if number < 10 and is_prime(number):
        return True
    elif number >= 10:
        last_digit = number % 10
        if last_digit == 0:
            return False
        remaining_number = number // 10
        if is_prime(remaining_number):
            return is_left_truncatable_prime(remaining_number)
    return False

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True