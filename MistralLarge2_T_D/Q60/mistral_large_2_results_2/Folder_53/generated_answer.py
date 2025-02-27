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

def all_left_right_truncatable_prime(t):
    x = t[86]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        temp = num
        while temp > 0 and is_prime(temp):
            temp = int(str(temp)[1:-1]) if len(str(temp)) > 2 else 0
        if temp == 0 and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)