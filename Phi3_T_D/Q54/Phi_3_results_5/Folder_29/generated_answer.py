def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(prime, primes_set):
    while prime > 0:
        if prime not in primes_set:
            return False
        prime = prime // 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    primes_set = {2}
    for num in range(3, x, 2):
        if is_prime(num):
            primes_set.add(num)
            if is_right_truncatable(num, primes_set):
                primes_set.add(num)
    return sorted(list(primes_set), reverse=True)