import math

def is_right_truncatable_prime(n):
    if n < 10 and n != 2 and (n != 3) and (n != 5) and (n != 7):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    output = []
    for n in numbers:
        if is_right_truncatable_prime(n):
            output.append(n)
    return sorted(output)