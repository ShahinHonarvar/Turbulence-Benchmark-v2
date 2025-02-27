def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        is_truncatable = True
        num_str = str(prime)
        while len(num_str) >= 2:
            if not is_prime(int(num_str)):
                is_truncatable = False
                break
            num_str = num_str[1:]
            num_str = num_str[:-1]
        if is_truncatable:
            truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes