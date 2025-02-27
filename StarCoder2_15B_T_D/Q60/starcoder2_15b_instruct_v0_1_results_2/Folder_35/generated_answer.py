def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for prime in numbers:
        is_truncatable = True
        str_prime = str(prime)
        for i in range(len(str_prime)):
            if i == 0:
                truncated_prime = int(str_prime[i + 1:])
            elif i == len(str_prime) - 1:
                truncated_prime = int(str_prime[:i])
            else:
                truncated_prime = int(str_prime[:i] + str_prime[i + 1:])
            if not is_prime(truncated_prime):
                is_truncatable = False
                break
        if is_truncatable:
            left_right_truncatable_primes.append(prime)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True