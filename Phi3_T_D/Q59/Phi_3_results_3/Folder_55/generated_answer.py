from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[73]
    left_truncatable = set()

    def is_left_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    for current in range(x, 1, -1):
        if is_left_truncatable(current):
            left_truncatable.add(current)
    return sorted(list(left_truncatable), reverse=True)