def all_right_truncatable_prime(tup):
    x = tup[35]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    right_trunc_primes = []
    for num in range(x - 1, 10 ** (len(str(x)) - 1) - 1, -1):
        if is_prime(num):
            is_rt_pruncatable = True
            truncated = num
            while is_prime(truncated):
                last_digit = str(truncated)[-1]
                truncated //= 10
                if truncated == 0:
                    is_rt_pruncatable = True
                    break
            if is_rt_pruncatable:
                right_trunc_primes.append(num)
    return right_trunc_primes