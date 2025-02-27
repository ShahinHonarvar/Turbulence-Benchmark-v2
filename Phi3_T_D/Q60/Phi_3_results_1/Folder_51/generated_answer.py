def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    truncatable_primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        if not num_str.startswith('0') and is_prime(num):
            if all((is_prime(int(num_str[i:])) and is_prime(int(num_str[:len(num_str) - i])) for i in range(len(num_str)))):
                truncatable_primes.append(num)
    return truncatable_primes