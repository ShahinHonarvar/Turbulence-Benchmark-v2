from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[93]
    result = []

    def is_left_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])):
                return False
        return True
    for potential in range(2, x):
        if is_left_truncatable(potential):
            result.append(potential)
    return result