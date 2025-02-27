def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for number in numbers:
        if is_left_right_truncatable_prime(number):
            left_right_truncatable_primes.append(number)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(number):
    if number < 10:
        return is_prime(number)
    if number % 10 == 0:
        return False
    if not is_prime(number):
        return False
    return is_left_right_truncatable_prime(number // 10)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True