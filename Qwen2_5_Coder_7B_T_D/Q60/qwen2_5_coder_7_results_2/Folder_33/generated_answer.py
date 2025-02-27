def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if int(str_n[i:]) not in primes or int(str_n[:-i]) not in primes:
                return False
        return True
    x = numbers[945]
    primes = {i for i in range(2, x + 1) if is_prime(i)}
    result = [n for n in primes if is_left_right_truncatable_prime(n)]
    return sorted(result, reverse=True)