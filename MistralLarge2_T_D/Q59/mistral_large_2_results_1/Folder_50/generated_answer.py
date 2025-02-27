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

def all_left_truncatable_prime(t):
    x = t[57]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = num
            while temp > 0:
                if temp not in primes:
                    break
                temp //= 10
            else:
                left_truncatable_primes.append(num)
                primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)