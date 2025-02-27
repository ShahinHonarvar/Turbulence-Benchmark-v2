def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, primes):
        str_n = str(n)
        for i in range(len(str_n), 0, -1):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = numbers[49]
    primes = [2, 3, 5, 7]
    prime_list = []
    for i in range(10, x):
        if primes[i % 4] != 0 and is_prime(i) and is_truncatable(i, primes):
            prime_list.append(i)
            primes[i % 4] = i
    return prime_list