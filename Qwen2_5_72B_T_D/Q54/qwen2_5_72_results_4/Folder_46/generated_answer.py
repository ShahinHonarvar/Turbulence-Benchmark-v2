def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_primes_below(n):
        primes = []
        for num in range(2, n):
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                primes.append(num)
        return primes
    x = numbers[33]
    return sorted(right_truncatable_primes_below(x))