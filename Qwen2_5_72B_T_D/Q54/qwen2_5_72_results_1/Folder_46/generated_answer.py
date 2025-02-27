from sympy import isprime

def all_right_truncatable_prime(numbers):

    def right_truncatable(n):
        for i in range(1, len(str(n)) + 1):
            if not isprime(int(str(n)[:i])):
                return False
        return True
    x = numbers[33]
    result = []
    for num in range(2, x):
        if right_truncatable(num):
            result.append(num)
    return sorted(result)