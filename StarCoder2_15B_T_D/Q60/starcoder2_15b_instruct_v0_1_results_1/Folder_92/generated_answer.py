def all_left_right_truncatable_prime(x):
    """
    Returns a list of all left-and-right-truncatable prime numbers less than or equal to x.
    """
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []
    right_truncatable_primes = []
    for i in range(10, x + 1):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            left_truncatable = True
            right_truncatable = True
            left_num = i
            right_num = i
            while left_num >= 10:
                if left_num % 2 == 0 or left_num % 3 == 0 or left_num % 5 == 0 or (left_num % 7 == 0):
                    left_truncatable = False
                    break
                left_num //= 10
            while right_num >= 10:
                if right_num % 10 == 2 or right_num % 10 == 4 or right_num % 10 == 5 or (right_num % 10 == 6) or (right_num % 10 == 8):
                    right_truncatable = False
                    break
                right_num //= 10
            if left_truncatable and right_truncatable:
                left_truncatable_primes.append(i)
                right_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)