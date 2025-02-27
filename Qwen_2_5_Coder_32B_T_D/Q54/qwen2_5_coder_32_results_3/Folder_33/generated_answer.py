def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[945]
    right_truncatable_primes = []
    for num in range(2, x):
        s = str(num)
        all_prime = True
        for i in range(len(s)):
            if not is_prime(int(s[:len(s) - i])):
                all_prime = False
                break
        if all_prime:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)