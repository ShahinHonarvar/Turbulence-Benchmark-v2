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

def is_left_right_truncatable(prime, tranche):
    if not prime.startswith('0') and (not prime.endswith('0')):
        if len(prime) > 1:
            for i in range(len(prime) - 1):
                if not is_prime(int(prime[i + 1:])) or not is_prime(int(prime[:i + 1])):
                    return False
        return True
    return False

def all_left_right_truncatable_prime(numbers):
    x = numbers[100]
    if x < 11:
        return []
    primitive_primes = [2, 3, 5, 7]
    found_primes = []
    for num in range(11, x + 1):
        if is_prime(num) and (not num in primitive_primes):
            if is_left_right_truncatable(str(num), str(num)):
                found_primes.append(num)
    return sorted(found_primes)