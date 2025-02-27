def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    num_str = str(n)
    if '0' in num_str:
        return False
    while len(num_str) > 1:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:-1]
    return is_prime(int(num_str))

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[42]
    primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)