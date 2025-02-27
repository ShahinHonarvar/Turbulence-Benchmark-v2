from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[77]
    left_truncatables = []
    for num in range(x - 1, 7, -1):
        if str(num)[0] in {'0', '2', '4', '5', '6', '8'} or not isprime(num):
            continue
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                break
        else:
            left_truncatables.append(num)
    return left_truncatables