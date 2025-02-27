def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[25]
    right_truncatable_primes = []
    for num in range(2, x):
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[:i + 1])):
                break
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)