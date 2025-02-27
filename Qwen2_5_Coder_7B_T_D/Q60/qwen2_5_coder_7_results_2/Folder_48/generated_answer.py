from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[835]
    primes = []
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num):
            num_str = str(num)
            while len(num_str) > 1:
                if not isprime(int(num_str[1:])) or not isprime(int(num_str[:-1])):
                    break
                num_str = num_str[1:-1]
            else:
                primes.append(num)
    return sorted(primes)