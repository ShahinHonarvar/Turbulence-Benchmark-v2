def all_left_right_truncatable_prime(numbers):
    x = numbers[37]
    truncatable_primes = [2, 3, 5, 7]
    for i in range(10, x + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            truncatable_primes.append(i)
    truncatable_primes = list(filter(lambda p: p > 9, truncatable_primes))
    for i in range(len(truncatable_primes)):
        p = truncatable_primes[i]
        while p >= 10:
            p = int(str(p)[1:])
            is_prime = True
            for j in range(2, int(p ** 0.5) + 1):
                if p % j == 0:
                    is_prime = False
                    break
            if not is_prime:
                truncatable_primes[i] = 0
                break
    truncatable_primes = list(filter(lambda p: p > 0, truncatable_primes))
    for i in range(len(truncatable_primes)):
        p = truncatable_primes[i]
        while p >= 10:
            p = int(str(p)[:-1])
            is_prime = True
            for j in range(2, int(p ** 0.5) + 1):
                if p % j == 0:
                    is_prime = False
                    break
            if not is_prime:
                truncatable_primes[i] = 0
                break
    truncatable_primes = list(filter(lambda p: p > 0, truncatable_primes))
    truncatable_primes.sort(reverse=True)
    return truncatable_primes