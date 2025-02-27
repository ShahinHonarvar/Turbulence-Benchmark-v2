def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    x = numbers[92]
    primes = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)