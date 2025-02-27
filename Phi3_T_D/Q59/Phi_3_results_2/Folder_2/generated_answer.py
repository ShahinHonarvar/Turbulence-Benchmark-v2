def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[618]
    truncable_primes = []
    p = [17, 37, 73, 313, 317, 373, 797, 3137, 3797, 739397]

    def is_truncatable_prime(num):
        truncated = str(num)
        while truncated:
            if not is_prime(int(truncated)):
                return False
            truncated = truncated[:-1]
        return True
    for prime in p:
        if prime < x and prime < 10:
            truncable_primes.append(prime)
    return truncable_primes