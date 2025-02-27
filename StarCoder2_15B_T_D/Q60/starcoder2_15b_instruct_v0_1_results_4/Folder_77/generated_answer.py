def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and left_right_truncatable_prime(int(str(n)[1:])) and left_right_truncatable_prime(int(str(n)[:-1]))

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for n in numbers:
        if left_right_truncatable_prime(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)