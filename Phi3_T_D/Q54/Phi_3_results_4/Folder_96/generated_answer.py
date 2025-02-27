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

def all_right_truncatable_prime(numbers):
    x = numbers[29]
    right_truncatable_primes = []
    for num in range(2, x):
        original_num = num
        while num > 0:
            if not is_prime(num):
                break
            num = num // 10
        if num == 0 and original_num != 2 and (original_num != 3):
            right_truncatable_primes.append(original_num)
    return sorted(right_truncatable_primes)