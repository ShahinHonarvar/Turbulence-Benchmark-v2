def all_left_truncatable_prime(numbers):
    x = numbers[65]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        for i in range(len(str(n))):
            if str(n)[i] == '0':
                return False
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    for num in range(11, x):
        if is_prime(num) and is_left_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)