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

def all_left_right_truncatable_prime(numbers):
    x = numbers[645]
    truncatable_primes = []
    for num in range(23, x + 1):
        num_str = str(num)
        if all((is_prime(int(num_str[i:])) for i in range(len(num_str)))) and all((is_prime(int(num_str[:i + 1])) for i in range(len(num_str)))):
            truncatable_primes.append(num)
    return truncatable_primes