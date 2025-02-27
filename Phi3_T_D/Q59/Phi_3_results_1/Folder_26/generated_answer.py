from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[81]
    prefixes = [str(num) for num in range(2, x) if isprime(num)]

    def is_left_truncatable(num, prefixes):
        for i in range(1, len(str(num))):
            if int(str(num)[i:]) not in prefixes:
                return False
        return True
    left_truncatables = [num for num in prefixes if is_left_truncatable(num, prefixes)]
    return sorted(left_truncatables, reverse=True)