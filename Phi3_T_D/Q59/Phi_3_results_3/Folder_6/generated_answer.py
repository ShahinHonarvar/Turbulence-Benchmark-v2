from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[74]
    truncatables = []
    for i in range(2, x):
        original_i = i
        while i > 0:
            if not isprime(i):
                break
            i = int(str(i)[1:])
        if i == 0:
            truncatables.append(original_i)
    return sorted(truncatables)