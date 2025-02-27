def all_left_truncatable_prime(numbers):
    x = numbers[784]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_left_truncatable(n):
        while n:
            if n in primes:
                n //= 10
            else:
                return False
        return True
    for num in range(11, x):
        if str(num).find('0') == -1 and is_prime(num):
            if check_left_truncatable(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)