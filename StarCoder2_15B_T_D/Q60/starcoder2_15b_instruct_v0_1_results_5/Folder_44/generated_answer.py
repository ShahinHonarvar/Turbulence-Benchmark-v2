def all_left_right_truncatable_prime(numbers):
    x = numbers[39]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_truncatable_prime(num):
    if num < 10:
        return is_prime(num)
    if not is_prime(num):
        return False
    return is_truncatable_prime(int(str(num)[1:])) and is_truncatable_prime(int(str(num)[:-1]))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True