def all_left_truncatable_prime(x):
    if x[92] <= 0:
        raise ValueError('The integer at index 92 must be positive.')
    left_truncatable_primes = []
    for i in range(2, x[92]):
        is_left_truncatable = True
        for j in range(len(str(i))):
            if not is_prime(int(str(i)[j:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True