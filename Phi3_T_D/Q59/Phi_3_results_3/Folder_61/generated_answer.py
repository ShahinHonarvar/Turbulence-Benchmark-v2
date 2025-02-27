import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[3]
    left_truncatables = []
    for i in range(2, x):
        num = str(i)
        if all((sympy.isprime(int(num[j:])) for j in range(len(num)))):
            left_truncatables.append(i)
    return sorted(left_truncatables, reverse=True)