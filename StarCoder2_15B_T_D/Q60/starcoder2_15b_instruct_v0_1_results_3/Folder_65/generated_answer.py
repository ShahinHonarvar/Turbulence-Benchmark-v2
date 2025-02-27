def all_left_right_truncatable_prime(x):
    x = x[32]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        temp = i
        while temp >= 10:
            if temp % 10 == 0:
                is_truncatable = False
                break
            temp //= 10
        temp = i
        while temp >= 10:
            if temp % 10 == 0:
                is_truncatable = False
                break
            temp //= 10
        if is_truncatable and all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            truncatable_primes.append(i)
    return truncatable_primes