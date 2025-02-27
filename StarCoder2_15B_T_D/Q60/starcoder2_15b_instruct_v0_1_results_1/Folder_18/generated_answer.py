import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[429]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            is_truncatable = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])) or not is_prime(int(str(i)[:-j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes