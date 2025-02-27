def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    if not t or t[42] < 2:
        return []
    left_right_truncatable_primes = []
    num = t[42]
    while num >= 10:
        if not is_prime(num):
            break
        num = num % 10 + num // 10
    if num == 2 or num == 3:
        left_right_truncatable_primes.append(t[42])
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes