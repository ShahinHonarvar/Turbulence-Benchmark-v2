from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[466]
    result = []
    for num in range(2, x):
        str_num = str(num)
        is_right_truncatable = True
        for i in range(len(str_num) - 1, 0, -1):
            if not isprime(int(str_num[:i])):
                is_right_truncatable = False
                break
        if is_right_truncatable and isprime(num):
            result.append(num)
    return sorted(result, reverse=True)