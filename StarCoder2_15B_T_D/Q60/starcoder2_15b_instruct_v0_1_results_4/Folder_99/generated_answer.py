def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for number in numbers:
        if is_truncatable_prime(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes)

def is_truncatable_prime(number):
    number_str = str(number)
    if not is_prime(number):
        return False
    if '0' in number_str:
        return False
    for i in range(1, len(number_str)):
        if not is_prime(int(number_str[i:])) or not is_prime(int(number_str[:len(number_str) - i])):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True