from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[370]

    def is_right_truncatable(n):
        while n:
            if not isprime(n):
                return False
            n //= 10
        return True
    result = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(result, reverse=True)