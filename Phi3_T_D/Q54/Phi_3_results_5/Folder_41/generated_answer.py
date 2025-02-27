def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(n):
    prime_list = [i for i in range(2, n + 1) if is_prime(i)]
    while prime_list and (not is_prime(prime_list[-1] // 10)):
        prime_list.pop()
    return prime_list