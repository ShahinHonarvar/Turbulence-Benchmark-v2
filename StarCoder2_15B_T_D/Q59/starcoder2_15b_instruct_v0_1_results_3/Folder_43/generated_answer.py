def all_left_truncatable_prime(args):
    numbers = args[0]
    x = numbers[89]
    left_truncatable_primes = []
    for number in numbers:
        if number < x and is_prime(number) and (not contains_zero(number)) and are_truncations_prime(number):
            left_truncatable_primes.append(number)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def contains_zero(number):
    return '0' in str(number)

def are_truncations_prime(number):
    while number > 0:
        if not is_prime(number):
            return False
        number //= 10
    return True