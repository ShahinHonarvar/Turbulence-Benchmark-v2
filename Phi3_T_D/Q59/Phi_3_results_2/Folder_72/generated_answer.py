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

def is_left_truncatable_prime(n, primes):
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_left_truncatable_prime(nr_tuple):
    prime_numbers = []
    for number in range(nr_tuple[31], 0, -1):
        s = str(number)
        if all(map(lambda char: char != '0', s)) and all((is_prime(int(s[i:])) for i in range(len(s)))):
            prime_numbers.append(number)
    return prime_numbers[::-1]