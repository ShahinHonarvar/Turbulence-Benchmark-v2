def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[177]
    primes = [2, 3, 5, 7]
    for i in range(10, x):
        if is_prime(i):
            primes.append(i)
            if is_left_truncatable_prime(i, list(primes)):
                for j in range(1, len(str(i))):
                    if not is_left_truncatable_prime(int(str(i)[j:]), primes):
                        primes.remove(i)
                        break
    return sorted(primes)