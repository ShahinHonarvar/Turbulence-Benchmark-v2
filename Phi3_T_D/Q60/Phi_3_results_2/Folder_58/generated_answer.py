def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(number, primes):
    if not all((digit not in ('0', '2', '4', '5', '6', '8') for digit in str(number))):
        return False
    for i in range(1, len(str(number))):
        if not (str(number)[i:] in primes and str(number)[:-i] in primes):
            return False
    return True

def get_all_left_and_right_truncatable_primes(threshold):
    primes = set(filter(is_prime, range(2, threshold + 1)))
    return sorted([prime for prime in primes if is_left_and_right_truncatable_prime(prime, primes)], reverse=True)

def all_left_right_truncatable_prime(numbers):
    x = numbers[975] if len(numbers) > 975 else 0
    return get_all_left_and_right_truncatable_primes(x)