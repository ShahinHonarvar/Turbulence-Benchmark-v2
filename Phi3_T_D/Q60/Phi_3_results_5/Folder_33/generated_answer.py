def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate(number):
        str_num = str(number)
        return [int(str_num[i:]) for i in range(len(str_num))] + [int(str_num[:i + 1]) for i in range(len(str_num))] if len(str_num) > 1 else []

    def is_truncatable_prime(number):
        return all((is_prime(t) for t in truncate(number)))
    limit = numbers[945]
    primes = [p for p in range(limit + 1) if is_prime(p) and is_truncatable_prime(p)]
    primes.sort(reverse=True)
    return primes