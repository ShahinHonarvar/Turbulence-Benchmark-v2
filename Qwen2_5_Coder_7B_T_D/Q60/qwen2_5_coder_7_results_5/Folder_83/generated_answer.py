from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[24]
    result = []
    primes = []

    def is_left_right_truncatable(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if '0' in str_num[i:]:
                return False
            if not isprime(int(str_num[i:])):
                return False
            if not isprime(int(str_num[:len(str_num) - i])):
                return False
        return True
    for num in range(2, x + 1):
        if isprime(num):
            primes.append(num)
            if is_left_right_truncatable(num):
                result.append(num)
    return sorted(result)