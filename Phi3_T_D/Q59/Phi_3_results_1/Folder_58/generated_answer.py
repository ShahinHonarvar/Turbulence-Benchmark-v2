def all_left_truncatable_prime(tuple_of_numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_of_numbers[975]
    left_truncatable_primes = []
    for number in range(x - 1, 1, -1):
        if '0' in str(number):
            continue
        if is_prime(number):
            s = str(number)
            if all((is_prime(int(s[i:])) for i in range(len(s)))):
                left_truncatable_primes.append(number)
    return left_truncatable_primes