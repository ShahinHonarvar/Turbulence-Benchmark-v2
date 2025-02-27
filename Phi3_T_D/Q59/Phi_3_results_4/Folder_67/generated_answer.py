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

def find_left_truncatable_primes(n):
    num_str = str(n)
    primes = []

    def is_left_truncatable(num, index):
        if not is_prime(int(num[index:])):
            return False
        if index == 0:
            return True
        return is_left_truncatable(num, index - 1)
    for i in range(n - 1, 10, -1):
        if '0' not in str(i) and is_left_truncatable(str(i), len(str(i)) - 1):
            primes.append(i)
    return primes

def all_left_truncatable_prime(*args):
    x = args[71] if len(args) > 71 else 0
    return find_left_truncatable_primes(x)