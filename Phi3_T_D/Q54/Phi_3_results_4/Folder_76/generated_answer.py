def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        if n not in primes:
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:-i])):
                return False
        return True
    truncatable_primes = []
    x = numbers[370]
    primes = [2]
    for num in range(3, x, 2):
        if is_prime(num):
            primes.append(num)
            if is_right_truncatable_prime(num, primes):
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)