def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, primes):
        str_n = str(n)
        for i in range(len(str_n)):
            if int(str_n[i:]) not in primes or int(str_n[:i + 1]) not in primes:
                return False
        return True
    limit = numbers[85]
    primes = [2, 3, 5, 7]
    possible = [2, 3, 5, 7]
    for num in range(11, limit + 1):
        if all((num % prime != 0 for prime in primes)):
            primes.append(num)
            possible.append(num)
    truncatable_primes = [prime for prime in possible if is_truncatable_prime(prime, primes)]
    return truncatable_primes