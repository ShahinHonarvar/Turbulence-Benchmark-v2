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

    def is_left_right_truncatable(n):
        n = str(n)
        if len(n) == 1 or len(n) == 2:
            return is_prime(int(n))
        if not is_prime(int(n)):
            return False
        left_truncs, right_truncs = (all_left_right_truncatable(n[1:]), all_left_right_truncatable(n[:-1]))
        if is_prime(int(n[1:])) and is_prime(int(n[:-1])):
            return True
        return False
    x = numbers[760]
    truncatable_primes = [p for p in range(2, x + 1) if is_left_right_truncatable(p)]
    return sorted(truncatable_primes, reverse=True)