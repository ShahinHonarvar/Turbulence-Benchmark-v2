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

def is_right_truncatable_prime(num, original_num):
    while num > 0:
        if not is_prime(num):
            return False
        num = num // 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    right_truncatable_primes = [i for i in range(x, 1, -1) if is_right_truncatable_prime(i, i)]
    return right_truncatable_primes