def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n, primes_set):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
            return False
    return int(str_n) in primes_set

def all_left_right_truncatable_primes(primes_range):
    max_num = primes_range[46]
    all_primes = set()
    for num in range(2, max_num + 1):
        if is_prime(num):
            all_primes.add(num)
    truncatable_primes = [prime for prime in all_primes if is_left_right_truncatable(prime, all_primes)]
    return sorted(truncatable_primes, reverse=True)