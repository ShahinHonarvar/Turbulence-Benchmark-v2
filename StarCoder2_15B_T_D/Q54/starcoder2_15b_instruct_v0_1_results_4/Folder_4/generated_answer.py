def all_right_truncatable_prime(numbers):
    x = numbers[96]
    right_truncatable_primes = []
    for i in range(1, x):
        num = i
        is_right_truncatable_prime = True
        while num > 0:
            if not is_prime(num):
                is_right_truncatable_prime = False
                break
            num //= 10
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True