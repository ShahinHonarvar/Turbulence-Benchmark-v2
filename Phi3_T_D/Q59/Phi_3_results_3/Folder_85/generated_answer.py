from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[94]
    left_truncatable = []

    def is_left_truncatable(number, digit_set=[2, 3, 5, 7]):
        str_num = str(number)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True
    for i in range(2, x):
        if is_left_truncatable(i):
            left_truncatable.append(i)
    return left_truncatable