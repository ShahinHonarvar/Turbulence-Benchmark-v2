from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[33]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if str(num).count('0') == 0:
            str_num = str(num)
            while len(str_num) > 0:
                if not isprime(int(str_num)):
                    break
                str_num = str_num[1:]
            else:
                str_num = str(num)
                while len(str_num) > 1:
                    if not isprime(int(str_num)):
                        break
                    str_num = str_num[:-1]
                else:
                    left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)