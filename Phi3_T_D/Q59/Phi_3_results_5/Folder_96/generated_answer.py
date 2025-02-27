def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n, sieve):
        if len(sieve) > 2 and sieve[len(sieve) - 1] == 0:
            return False
        if not is_prime(n):
            return False
        if not str(n).lstrip('0').isdigit():
            return False
        if all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n))))):
            return True
        return False
    x = numbers[29]
    sieve = [True] * (x + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, x + 1, i):
                sieve[j] = False
    return [i for i in range(x) if left_truncatable(i, sieve)]