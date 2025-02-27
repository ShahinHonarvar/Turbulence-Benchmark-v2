def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, prime_numbers):
        str_n = str(n)
        for i in range(len(str_n)):
            if is_prime(int(str_n[i:])):
                pass
            else:
                return False
        return True
    x = numbers[96]
    primes = [2, 3, 5, 7]
    for number in range(11, x, 2):
        if is_prime(number):
            primes.append(number)
    left_truncatable_primes = []
    for prime in primes:
        if is_left_truncatable_prime(prime, primes):
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes