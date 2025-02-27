def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[74]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            s = str(num)
            for i in range(len(s) - 1, 0, -1):
                if not is_prime(int(s[:i])):
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)