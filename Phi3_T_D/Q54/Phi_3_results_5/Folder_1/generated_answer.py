def all_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(prime, primes_set):
        str_prime = str(prime)
        while str_prime:
            if not is_prime(int(str_prime)):
                return False
            primes_set.add(prime)
            str_prime = str_prime[:-1]
        return True
    primes_set = set()
    x = numbers[19]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable_prime(num, primes_set):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)