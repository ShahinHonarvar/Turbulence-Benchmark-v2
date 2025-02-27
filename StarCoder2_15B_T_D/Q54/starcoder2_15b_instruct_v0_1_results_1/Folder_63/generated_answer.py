import math

def all_right_truncatable_prime(numbers):
    x = numbers[88]
    right_truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            truncated_prime = i
            while truncated_prime >= 10:
                truncated_prime //= 10
                if truncated_prime == 0 or not is_prime_number(truncated_prime):
                    is_prime = False
                    break
            if is_prime:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True