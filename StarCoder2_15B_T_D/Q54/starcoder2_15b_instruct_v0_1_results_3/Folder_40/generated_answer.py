def all_right_truncatable_prime(input_tuple):
    x = input_tuple[10]

    def is_right_truncatable_prime(num):
        if num < 2:
            return False
        if num in (2, 3):
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes