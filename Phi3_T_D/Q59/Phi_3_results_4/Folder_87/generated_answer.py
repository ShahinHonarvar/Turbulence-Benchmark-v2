import sympy

def is_truncatable_prime(number):
    str_num = str(number)
    return all((sympy.isprime(int(str_num[i:])) for i in range(len(str_num))))

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    return sorted([p for p in range(2, x) if is_truncatable_prime(p)], reverse=True)