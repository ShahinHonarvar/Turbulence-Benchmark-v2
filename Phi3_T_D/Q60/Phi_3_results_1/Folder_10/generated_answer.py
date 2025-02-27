def all_left_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if input_tuple[38] < 11:
        return []
    truncatable_primes = []
    for num in range(11, input_tuple[38] + 1, 2):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)

def is_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    while n < 10:
        if n < 2 or not is_prime(n):
            return False
        n = n // 10
    return True