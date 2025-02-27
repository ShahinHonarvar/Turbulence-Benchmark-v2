def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[67]
    right_truncatable_primes = []
    for num in range(2, x):
        is_right_truncatable = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[:len(str(num)) - i])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)