def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[975] if len(numbers) > 975 else None
    if x is None:
        return []
    right_truncatable_primes = []
    primes_set = {2, 3, 5, 7}
    for num in range(5, x):
        s = str(num)
        if any((int(s[:i]) not in primes_set for i in range(len(s), 0, -1))):
            continue
        if not all((is_prime(int(s[:i])) for i in range(len(s), 0, -1))):
            continue
        if num in primes_set:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)