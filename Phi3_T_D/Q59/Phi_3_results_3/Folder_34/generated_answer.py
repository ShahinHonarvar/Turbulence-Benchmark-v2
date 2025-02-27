def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(prime):
        for i in range(len(prime)):
            if not is_prime(int(prime[i:])):
                return False
        return True
    x = numbers[18]
    trunc_primes = []
    for number in range(x - 1, 1, -1):
        if is_prime(number):
            if is_left_truncatable(str(number)):
                trunc_primes.append(number)
    return trunc_primes