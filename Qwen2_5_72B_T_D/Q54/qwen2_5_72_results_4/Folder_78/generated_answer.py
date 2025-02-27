def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[23]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            is_truncatable = True
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes)