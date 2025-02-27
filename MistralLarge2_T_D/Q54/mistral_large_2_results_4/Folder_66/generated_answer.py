def all_right_truncatable_prime(t):

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
                truncatable = True
                temp = num
                while temp > 0:
                    if not is_prime(temp):
                        truncatable = False
                        break
                    temp //= 10
                if truncatable:
                    primes.append(num)
        return primes
    x = t[25]
    right_truncatable_primes = generate_right_truncatable_primes(x)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes