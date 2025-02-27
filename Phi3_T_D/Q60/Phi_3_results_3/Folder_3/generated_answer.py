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

def all_left_right_truncatable_primes(numbers):
    upper_limit = numbers[100]
    truncatable_primes = []

    def is_left_and_right_truncatable(prime, primes_set):
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:-i])):
                return False
        return True
    primes_set = set()
    for num in range(2, upper_limit + 1):
        if is_prime(num):
            primes_set.add(num)
            if is_left_and_right_truncatable(num, primes_set):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)