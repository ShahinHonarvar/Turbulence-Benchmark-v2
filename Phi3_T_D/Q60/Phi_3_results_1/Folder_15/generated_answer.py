def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(prime):
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:i])):
                return False
        return True
    x = numbers[6]
    truncatable_primes = []
    for number in range(x, 1, -1):
        if is_prime(number) and is_truncatable_prime(number):
            truncatable_primes.append(number)
    return truncatable_primes