def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[87]
    primes = [2, 3, 5, 7]
    result = []

    def is_right_truncatable(prime):
        while prime > 0:
            if not is_prime(prime):
                return False
            prime //= 10
        return True
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable(num):
            result.append(num)
    return sorted(result)