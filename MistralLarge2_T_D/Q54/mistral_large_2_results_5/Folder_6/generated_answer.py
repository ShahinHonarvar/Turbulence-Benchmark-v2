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

def generate_right_truncatable_primes(limit):
    right_truncatable_primes = []
    for i in range(2, limit):
        if is_prime(i):
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                right_truncatable_primes.append(i)
    return right_truncatable_primes

def all_right_truncatable_prime(numbers):
    x = numbers[74]
    right_truncatable_primes = generate_right_truncatable_primes(x)
    return sorted(right_truncatable_primes)