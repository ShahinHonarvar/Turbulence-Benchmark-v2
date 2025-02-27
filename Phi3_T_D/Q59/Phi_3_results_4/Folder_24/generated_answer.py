def is_prime(n):
    if n <= 1:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True

def all_left_truncatable_prime(bounds):
    x = bounds[65]
    truncatable_primes = []
    for num in range(x, 1, -1):
        if not any((digit == '0' for digit in str(num))):
            if is_prime(num):
                is_truncatable = True
                temp = str(num)
                while temp:
                    temp = temp[:-1]
                    if not is_prime(int(temp)):
                        is_truncatable = False
                        break
                if is_truncatable:
                    truncatable_primes.append(num)
    return truncatable_primes