def all_left_truncatable_prime(numbers):
    x = numbers[29]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    left_truncatable_primes = []
    for prime in primes:
        is_left_truncatable = True
        s = str(prime)
        if '0' in s:
            continue
        for i in range(len(s)):
            if int(s[i:]) not in primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)