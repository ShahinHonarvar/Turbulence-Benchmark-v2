def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[466]
    lr_truncatable_primes = []
    for num in range(23, x + 1):
        n = str(num)
        if '0' not in n:
            if all((is_prime(int(n[i:])) and is_prime(int(n[:len(n) - i])) for i in range(1, len(n)))):
                lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes, reverse=True)