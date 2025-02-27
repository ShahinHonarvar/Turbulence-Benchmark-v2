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
    x = t[18]
    primes = [2, 3, 5, 7]
    for num in range(11, x):
        if '0' not in str(num) and is_prime(num):
            is_left_truncatable = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)