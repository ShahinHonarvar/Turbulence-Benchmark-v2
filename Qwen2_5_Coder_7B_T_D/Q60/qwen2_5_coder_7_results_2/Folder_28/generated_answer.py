from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[19]
    truncatable_primes = []
    primes = [2, 3, 5, 7]

    def is_truncatable_prime(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if int(str_num[i:]) not in primes or int(str_num[:i + 1]) not in primes:
                return False
        return True
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)