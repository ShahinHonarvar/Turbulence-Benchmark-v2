def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(primes):
        truncs = set(primes)
        for p in primes:
            p_str = str(p)
            for i in range(1, len(p_str)):
                if int(p_str[i:]) not in truncs or int(p_str[:-i]) not in truncs:
                    return False
        return True
    x = numbers[792]
    primes = [p for p in range(2, x + 1) if is_prime(p)]
    left_right_truncs = [p for p in primes if is_truncatable({p})]
    return left_right_truncs