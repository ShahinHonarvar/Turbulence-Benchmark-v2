def is_left_and_right_truncatable(prime, primes_set):
    nstr = str(prime)
    for i in range(len(nstr)):
        if int(nstr[i:]) not in primes_set or int(nstr[:-i or None]) not in primes_set:
            return False
    return True

def all_left_right_truncatable_prime(integers):
    if not (0 < len(integers) <= 2 and integers[0] <= integers[1]):
        return []
    start, end = integers
    if start > 7 or end < 11:
        return []
    primes = set(filter(is_prime, range(start, end + 1)))
    truncatable_primes = [p for p in primes if is_left_and_right_truncatable(p, primes)]
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True