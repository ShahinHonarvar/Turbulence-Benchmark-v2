def all_right_truncatable_prime(numbers):
    x = numbers[945]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(10, x):
        if is_prime(num):
            while num > 0:
                if not is_prime(num):
                    break
                num //= 10
            else:
                primes.append(num)
    return sorted(primes, reverse=True)