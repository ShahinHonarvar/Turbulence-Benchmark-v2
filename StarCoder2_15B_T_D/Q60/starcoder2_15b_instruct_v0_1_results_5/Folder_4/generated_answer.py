def is_left_right_truncatable_prime(number):
    number_str = str(number)
    if '0' in number_str:
        return False
    truncations = [number_str[i:] for i in range(len(number_str))] + [number_str[:-i] for i in range(1, len(number_str))]
    for truncation in truncations:
        if not is_prime(int(truncation)):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for number in numbers:
        if is_left_right_truncatable_prime(number):
            left_right_truncatable_primes.append(number)
    return sorted(left_right_truncatable_primes, reverse=True)