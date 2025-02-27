import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[992]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            truncated = i
            while truncated > 9:
                truncated //= 10
                if not is_prime(truncated):
                    break
            else:
                truncated = i
                while truncated > 9:
                    truncated = truncated % 10 ** (len(str(truncated)) - 1)
                    if not is_prime(truncated):
                        break
                else:
                    truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes