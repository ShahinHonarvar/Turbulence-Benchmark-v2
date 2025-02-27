def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, prime_digits):
        if n < 10:
            return False
        n_str = str(n)
        for i in range(len(n_str)):
            if n_str[i] in prime_digits and is_prime(int(n_str[i:])):
                if len(n_str) - i > 1 or n_str[i + 1:] == '':
                    return is_truncatable_prime(int(n_str[i + 1:]), prime_digits)
        return False
    x = numbers[33]
    prime_digits = {'2', '3', '5', '7'}
    truncatable_primes = []
    for number in range(2, x):
        if is_prime(number) and is_truncatable_prime(number, prime_digits):
            truncatable_primes.append(number)
    return truncatable_primes