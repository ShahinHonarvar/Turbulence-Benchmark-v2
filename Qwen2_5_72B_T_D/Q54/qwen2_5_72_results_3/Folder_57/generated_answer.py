def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_primes(limit):
        primes = []
        for n in range(2, limit):
            all_prime = True
            for i in range(1, len(str(n)) + 1):
                if not is_prime(int(str(n)[:i])):
                    all_prime = False
                    break
            if all_prime:
                primes.append(n)
        return primes
    x = numbers[54]
    result = right_truncatable_primes(x)
    return sorted(result, reverse=True)