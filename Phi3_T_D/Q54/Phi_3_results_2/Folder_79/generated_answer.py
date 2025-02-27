from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[91]
    truncatables = set()
    for num in range(2, x):
        if isprime(num):
            s = str(num)
            if all((isprime(int(s[:i])) for i in range(1, len(s)))):
                truncatables.add(num)
    return sorted(truncatables)