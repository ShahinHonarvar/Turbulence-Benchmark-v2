def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for number in numbers:
        if is_truncatable_prime(number):
            left_right_truncatable_primes.append(number)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_truncatable_prime(number):
    if not is_prime(number):
        return False
    number_str = str(number)
    if '0' in number_str:
        return False
    for i in range(len(number_str) - 1):
        if not is_prime(int(number_str[i + 1:])) or not is_prime(int(number_str[:i + 1])):
            return False
    return True

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True