from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[30]
    right_truncatables = []

    def is_right_truncatable(number, x):
        for i in range(len(str(number))):
            if not isprime(number):
                return False
            number //= 10
        return number == 0 and number < x
    for number in range(x - 1, 1, -1):
        if is_right_truncatable(number, x):
            right_truncatables.append(number)
    return right_truncatables[::-1]