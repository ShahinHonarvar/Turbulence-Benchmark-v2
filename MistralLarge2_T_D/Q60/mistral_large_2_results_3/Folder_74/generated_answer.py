def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable(prime):
    prime_str = str(prime)
    if '0' in prime_str:
        return False
    while len(prime_str) > 1:
        prime_str = prime_str[1:-1]
        if not is_prime(int(prime_str)):
            return False
    return True

def all_left_right_truncatable_prime(data):
    x = data[36]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)