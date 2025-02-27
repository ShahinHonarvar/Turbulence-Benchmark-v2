def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[758]
    truncatable_primes = []
    for i in range(2, x + 1):
        if not is_prime(i):
            continue
        str_i = str(i)
        if not all((str(i).startswith(str(j)) and is_prime(int(str(j))) for j in range(1, 10))):
            continue
        if not all((str(i).endswith(str(j)) and is_prime(int(str(i)[:-j])) for j in range(1, len(str(i)) + 1))):
            continue
        truncatable_primes.append(i)
    return sorted(truncatable_primes)