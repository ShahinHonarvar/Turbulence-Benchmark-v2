def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    truncatable_primes = []
    for prime in (p for p in range(2, x + 1) if is_prime(p)):
        p_str = str(prime)
        if '0' in p_str:
            continue
        is_truncatable = True
        while len(p_str) > 1 and is_truncatable:
            if is_prime(int(p_str)) and is_prime(int(p_str[-1:])):
                p_str = p_str[-1:]
            else:
                is_truncatable = False
        if is_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)