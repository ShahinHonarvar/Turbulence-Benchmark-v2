def all_right_truncatable_prime(tuples):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(num, sieve):
        if num == 0:
            return True
        if not sieve[num % 10]:
            return False
        return is_right_truncatable(num // 10, sieve)
    primes_limit = tuples[92]
    sieve = [True] * (primes_limit + 1)
    for p in range(2, int(primes_limit ** 0.5) + 1):
        if sieve[p]:
            for i in range(p * p, primes_limit + 1, p):
                sieve[i] = False
    truncatable_primes = set()
    for num in range(7, primes_limit, 2):
        stack = []
        temp_num = num
        while temp_num > 0:
            stack.append(temp_num)
            temp_num //= 10
        while stack:
            if not is_prime(stack.pop()):
                break
        if not stack and is_right_truncatable(num, sieve):
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes))