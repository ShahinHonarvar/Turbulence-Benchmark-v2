def all_left_truncatable_prime(numbers):
    x = numbers[70]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if int(str_n[i:]) not in primes:
                return False
        return True
    for num in range(2, x):
        if str(num).count('0') == 0 and is_prime(num):
            primes.append(num)
    return sorted([num for num in primes if is_left_truncatable_prime(num)])