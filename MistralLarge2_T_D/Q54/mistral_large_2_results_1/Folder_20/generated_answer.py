def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    right_truncatable_primes = []
    for num in range(2, x):
        temp = num
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)