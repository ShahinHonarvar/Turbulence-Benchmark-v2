def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:i])):
                return False
        return True
    x = numbers[54]
    trunc_primes = [i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)]
    return sorted(trunc_primes, reverse=True)