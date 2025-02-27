def all_left_right_truncatable_prime(x):
    primes = [True] * (x + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, x + 1, i):
                primes[j] = False

    def is_left_right_truncatable(num):
        num_str = str(num)
        while len(num_str) > 1:
            if not primes[int(num_str)]:
                return False
            num_str = num_str[1:]
            num_str = num_str[:-1]
        return True
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if primes[num] and is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes