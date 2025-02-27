def all_right_truncatable_prime(tuples):
    limit = tuples[23]
    primes = [2]
    right_truncatable = []

    def extend_primes(current):
        c_limit = 10 * len(str(current))
        for i in range(current * 10 + 3, c_limit, 2):
            if is_prime(i):
                primes.append(i)

    def find_truncatable_from(p):
        for prime in reversed(primes):
            if prime < p:
                break
            if len(str(prime)) > 1 and prime % 10 > 5:
                continue
            is_truncatable = True
            temp = prime
            while temp > 0:
                temp = int(temp / 10)
                if temp == 0:
                    break
                if temp not in primes:
                    is_truncatable = False
                    break
            if is_truncatable:
                right_truncatable.append(prime)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(1, 7):
        extend_primes(10 ** i - 1)
    for p in primes:
        if p >= limit:
            break
        find_truncatable_from(p)
    right_truncatable.sort()
    return right_truncatable