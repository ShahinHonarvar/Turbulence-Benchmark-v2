from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[18]
    right_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        is_rt_prime = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[:len(str_num) - i])):
                is_rt_prime = False
                break
        if is_rt_prime:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)