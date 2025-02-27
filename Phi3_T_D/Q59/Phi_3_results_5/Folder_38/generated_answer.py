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

def is_left_truncatable_prime(n, primes):
    return all((p in primes for p in map(int, [n[i:] for i in range(len(n))])))

def all_left_truncatable_prime(integers):
    x = integers[28]
    primes = [2]
    for i in range(3, x, 2):
        if is_prime(i):
            primes.append(i)
            p = str(i)
            is_truncatable = True
            for j in range(len(p)):
                if not is_prime(int(p[j:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted([p for p in primes if len(str(p)) >= 2])