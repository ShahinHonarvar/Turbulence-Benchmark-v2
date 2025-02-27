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
    x = numbers[100]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []
    for num in range(7, x, 2):
        if is_prime(num):
            num_str = str(num)
            for i in range(len(num_str) - 1, -1, -1):
                if is_prime(int(num_str[:i + 1])):
                    right_truncatable_primes.append(num)
                else:
                    break
    return sorted(set(filter(lambda p: p in primes, right_truncatable_primes)))