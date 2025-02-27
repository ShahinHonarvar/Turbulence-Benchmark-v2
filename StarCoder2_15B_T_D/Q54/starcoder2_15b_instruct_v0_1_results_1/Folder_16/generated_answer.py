def all_right_truncatable_prime(x):
    if not isinstance(x, tuple) or len(x) != 1 or (not isinstance(x[0], int)) or (x[0] <= 0):
        return []
    x = x[0]
    if x <= 792:
        return []
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable_prime = True
        for j in range(len(str(i))):
            if not is_prime(int(str(i)[j:])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True