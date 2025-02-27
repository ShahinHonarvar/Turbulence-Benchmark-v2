from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[3]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if isprime(num):
            temp = num
            while temp >= 10:
                temp = int(str(temp)[1:])
                if not isprime(temp):
                    break
            else:
                temp = num
                while temp >= 10:
                    temp = int(str(temp)[:-1])
                    if not isprime(temp):
                        break
                else:
                    left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)