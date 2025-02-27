def all_right_truncatable_prime(numbers):
    max_num = numbers[24]
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n, primes):
        str_n = str(n)
        for i in range(len(str_n), 0, -1):
            if not is_prime(int(str_n[:i])):
                return False
        return True
    primes = set()
    for num in range(2, max_num):
        if is_prime(num):
            primes.add(num)
            if is_right_truncatable(num, primes):
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)