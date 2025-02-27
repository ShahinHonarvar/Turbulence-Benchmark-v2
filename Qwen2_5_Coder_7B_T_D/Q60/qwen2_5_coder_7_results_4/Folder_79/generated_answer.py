from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[91]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if isprime(num) and '0' not in str(num):
            str_num = str(num)
            is_truncatable = True
            for i in range(1, len(str_num)):
                if not isprime(int(str_num[i:])) or not isprime(int(str_num[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes)