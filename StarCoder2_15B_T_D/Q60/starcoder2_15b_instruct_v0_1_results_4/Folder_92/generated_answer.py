def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[0]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            num_digits = len(str(i))
            j = i
            while num_digits > 1:
                j //= 10
                if not is_prime(j):
                    break
                num_digits -= 1
            if num_digits == 1:
                truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes