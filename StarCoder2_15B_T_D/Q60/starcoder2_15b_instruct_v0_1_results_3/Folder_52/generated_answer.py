def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    truncatable_primes = []
    for p in primes:
        p_str = str(p)
        if '0' in p_str:
            continue
        is_truncatable = True
        for i in range(len(p_str) - 1):
            if not is_prime(int(p_str[i + 1:])) or not is_prime(int(p_str[:len(p_str) - i - 1])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(p)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes