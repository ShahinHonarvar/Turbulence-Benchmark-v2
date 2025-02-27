import math

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[4]
    right_truncatable_primes = []
    for number in range(2, x):
        is_prime = True
        for divisor in range(2, int(math.sqrt(number)) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            remaining_number = number
            while remaining_number > 0:
                if not is_prime_number(remaining_number):
                    is_prime = False
                    break
                remaining_number //= 10
        if is_prime:
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)

def is_prime_number(number):
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True