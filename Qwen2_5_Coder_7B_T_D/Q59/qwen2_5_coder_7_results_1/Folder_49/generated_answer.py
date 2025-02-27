def all_left_truncatable_prime(numbers):
    x = numbers[14]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        str_n = str(n)
        while str_n:
            if '0' in str_n or not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable(num):
            primes.append(num)
    return sorted(primes)