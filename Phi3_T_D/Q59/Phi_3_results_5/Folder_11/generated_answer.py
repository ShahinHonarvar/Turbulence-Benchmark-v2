from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[86]
    left_truncatables = []
    for number in range(2, x):
        original_number = number
        while number > 0:
            if not isprime(number):
                break
            number = number // 10
        if number == 0 and isprime(original_number):
            left_truncatables.append(original_number)
    return left_truncatables