from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for num in range(x - 1, 0, -1):
        str_num = str(num)
        if all((isprime(int(str_num[i:])) for i in range(len(str_num)))):
            primes.append(num)
    return sorted(primes, reverse=True)