from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[126]
    limit = int('1' + '9' * 9 + '8' * 8 + '7' * 7 + '6' * 6 + '5' * 5 + '4' * 4 + '3' * 3 + '2' * 2 + '1')
    left_truncatable_primes = [2, 3, 5, 7]
    for num in range(10, limit):
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num))))) and '0' not in str(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)