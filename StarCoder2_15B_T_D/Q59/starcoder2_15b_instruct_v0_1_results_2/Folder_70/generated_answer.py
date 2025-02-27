def all_left_truncatable_prime(input_tuple):
    x = input_tuple[433]
    if x <= 0:
        return []
    primes = []
    for num in range(2, x):
        if is_prime(num):
            primes.append(num)
    left_truncatable_primes = []
    for prime in primes:
        is_left_truncatable = True
        temp = prime
        while temp > 0:
            if not is_prime(temp):
                is_left_truncatable = False
                break
            temp //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True