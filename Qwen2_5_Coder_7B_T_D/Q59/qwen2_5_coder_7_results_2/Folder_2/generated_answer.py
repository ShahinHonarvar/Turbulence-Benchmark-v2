def all_left_truncatable_prime(input_tuple):
    x = input_tuple[618]
    primes = []
    for num in range(2, x):
        if all((int(digit) != 0 and is_prime(int(str(num)[:i + 1])) for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True