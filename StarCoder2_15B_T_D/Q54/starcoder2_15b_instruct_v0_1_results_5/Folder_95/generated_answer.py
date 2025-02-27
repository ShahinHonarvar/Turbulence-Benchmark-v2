def all_right_truncatable_prime(t):
    x = t[0]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable = True
        for j in range(len(str(i)) - 1, 0, -1):
            if not is_prime(int(str(i)[:j])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True