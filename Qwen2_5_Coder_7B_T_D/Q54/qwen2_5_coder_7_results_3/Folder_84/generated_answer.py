def all_right_truncatable_prime(t):
    x = t[630]
    primes = []
    for num in range(2, x):
        if all((int(num) % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            num_str = str(num)
            is_right_truncatable = True
            for i in range(1, len(num_str)):
                if int(num_str[:-i]) % i != 0:
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)