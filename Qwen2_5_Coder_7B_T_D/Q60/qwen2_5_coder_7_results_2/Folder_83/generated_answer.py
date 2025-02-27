from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[24]
    primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and isprime(num):
            str_num = str(num)
            while len(str_num) > 1:
                if not isprime(int(str_num[1:])) or not isprime(int(str_num[:-1])):
                    break
                str_num = str_num[1:-1]
            else:
                primes.append(num)
    return sorted(primes)