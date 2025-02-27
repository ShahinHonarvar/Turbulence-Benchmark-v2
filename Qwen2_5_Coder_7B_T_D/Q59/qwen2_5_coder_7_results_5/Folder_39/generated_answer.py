def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    for i in range(len(str(num))):
        if not is_prime(int(str(num)[i:])):
            return False
    return is_prime(num)

def all_left_truncatable_prime(numbers):
    x = numbers[30]
    left_truncatable_primes = [num for num in range(10, x) if left_truncatable_prime(num) and '0' not in str(num)]
    return sorted(left_truncatable_primes, reverse=True)