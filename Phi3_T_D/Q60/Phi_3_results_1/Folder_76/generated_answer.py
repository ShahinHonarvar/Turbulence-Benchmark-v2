def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    if not is_prime(n):
        return False
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(primes):
    x = primes[370]
    return sorted([p for p in range(2, x + 1) if is_left_right_truncatable_prime(p)], reverse=True)

def generate_primes(n):
    is_prime = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes