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

def all_right_truncatable_prime(tup):
    primes = []
    x = tup[1]
    for i in range(7, x, 2):
        prime_truncatable = True
        num = i
        while num > 0:
            if not is_prime(num):
                prime_truncatable = False
                break
            num = num // 10
        if prime_truncatable:
            primes.append(i)
    primes.sort(reverse=True)
    return primes