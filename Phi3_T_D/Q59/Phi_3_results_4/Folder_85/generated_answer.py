def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[94]
    left_truncatable_primes = []
    for n in range(2, x):
        if is_prime(n):
            original_n = n
            while n > 0:
                if not is_prime(int(str(n)[:-1])):
                    break
                n = int(str(n)[1:])
            else:
                left_truncatable_primes.append(original_n)
    return left_truncatable_primes