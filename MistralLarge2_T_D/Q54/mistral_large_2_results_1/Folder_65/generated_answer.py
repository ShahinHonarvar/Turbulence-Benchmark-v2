def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_right_truncatable_primes(limit):
        primes = []
        for num in range(2, limit):
            if is_prime(num):
                temp = num
                while temp > 0:
                    if not is_prime(temp):
                        break
                    temp //= 10
                else:
                    primes.append(num)
        return primes
    x = numbers[32]
    return sorted(generate_right_truncatable_primes(x))