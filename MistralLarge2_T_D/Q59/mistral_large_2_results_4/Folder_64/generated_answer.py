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

def all_left_truncatable_prime(t):
    x = t[4]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        temp = num
        is_left_truncatable = True
        while temp > 0:
            if not is_prime(temp):
                is_left_truncatable = False
                break
            temp //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)