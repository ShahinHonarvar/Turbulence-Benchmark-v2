def all_left_right_truncatable_prime(t):
    x = t[835]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(10, x + 1):
        if is_prime(i):
            num_str = str(i)
            is_truncatable = True
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[j:])) or not is_prime(int(num_str[:-j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)