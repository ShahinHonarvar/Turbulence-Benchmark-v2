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

def all_left_truncatable_prime(numbers):
    x = numbers[8]
    limit = 10 ** (len(str(x)) - 1)
    primes = [i for i in range(2, limit) if is_prime(i) and '0' not in str(i)]
    left_truncatable_primes = []
    for prime in primes:
        temp = prime
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes