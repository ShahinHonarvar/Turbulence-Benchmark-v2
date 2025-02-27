def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for number in numbers:
        if is_left_right_truncatable_prime(number):
            left_right_truncatable_primes.append(number)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_left_right_truncatable_prime(number):
    if not is_prime(number):
        return False
    digits = [int(digit) for digit in str(number)]
    for i in range(len(digits) - 1):
        left_truncatable = int(''.join((str(digit) for digit in digits[i:])))
        right_truncatable = int(''.join((str(digit) for digit in digits[:i + 1])))
        if not is_prime(left_truncatable) or not is_prime(right_truncatable):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True