def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for number in numbers:
        if is_left_right_truncatable_prime(number):
            left_right_truncatable_primes.append(number)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_left_right_truncatable_prime(number):
    if not is_prime(number):
        return False
    digits = [int(d) for d in str(number)]
    while len(digits) > 1:
        if digits[0] == 0 or digits[-1] == 0:
            return False
        if not is_prime(int(''.join(map(str, digits)))):
            return False
        digits = digits[1:]
        digits = digits[:-1]
    return True

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True