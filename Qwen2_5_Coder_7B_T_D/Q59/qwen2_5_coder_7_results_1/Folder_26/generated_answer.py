from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[81]
    left_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' not in str_num and all((isprime(int(str_num[:i + 1])) for i in range(len(str_num)))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)