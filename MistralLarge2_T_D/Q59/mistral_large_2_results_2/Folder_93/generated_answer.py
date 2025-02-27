def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[11]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = []
    for p in primes:
        num = p
        while num > 0:
            if not is_prime(num):
                break
            if '0' in str(num):
                break
            num = int(str(num)[1:]) if num >= 10 else 0
        else:
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes)