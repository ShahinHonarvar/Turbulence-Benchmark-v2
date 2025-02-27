def all_left_right_truncatable_prime(tup):
    x = tup[98]
    left_truncatable_primes = [2, 3, 5, 7]
    right_truncatable_primes = [2, 3, 5, 7]
    for i in range(1, x + 1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or (i % 7 == 0):
            continue
        left_truncatable_prime = True
        num = i
        while num > 0:
            if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
                left_truncatable_prime = False
                break
            num //= 10
        if left_truncatable_prime:
            left_truncatable_primes.append(i)
        right_truncatable_prime = True
        num = i
        while num > 0:
            if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
                right_truncatable_prime = False
                break
            num %= 10
        if right_truncatable_prime:
            right_truncatable_primes.append(i)
    left_right_truncatable_primes = [p for p in left_truncatable_primes if p in right_truncatable_primes]
    return sorted(left_right_truncatable_primes)