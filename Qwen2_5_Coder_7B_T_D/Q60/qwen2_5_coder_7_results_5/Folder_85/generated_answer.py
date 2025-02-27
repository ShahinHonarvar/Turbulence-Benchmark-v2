from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[94]
    primes = [i for i in range(2, x + 1) if isprime(i) and '0' not in str(i)]
    truncatable_primes = []
    for num in primes:
        str_num = str(num)
        while len(str_num) > 1 and isprime(int(str_num)):
            str_num = str_num[1:]
        if len(str_num) <= 2 and isprime(int(str_num)):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)