from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[78]
    primes = [num for num in range(2, x + 1) if isprime(num)]

    def is_left_right_truncatable(num):
        if '0' in str(num):
            return False
        num_str = str(num)
        while len(num_str) > 1:
            if not isprime(int(num_str)):
                return False
            num_str = num_str[1:-1]
        return isprime(int(num_str)) if num_str else False
    return sorted([p for p in primes if is_left_right_truncatable(p)], reverse=True)