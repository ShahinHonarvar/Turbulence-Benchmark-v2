def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[465]
    left_truncatables = []

    def generate_primes(n):
        if n < 2 or n < 0 or n >= x:
            return
        if is_prime(n):
            for i in range(1, len(str(n))):
                left_truncatable = int(str(n)[:i])
                if left_truncatable != 0 and is_prime(left_truncatable):
                    left_truncatables.append(left_truncatable)
            generate_primes(n + 1)
    generate_primes(2)
    left_truncatables.sort(reverse=True)
    return left_truncatables