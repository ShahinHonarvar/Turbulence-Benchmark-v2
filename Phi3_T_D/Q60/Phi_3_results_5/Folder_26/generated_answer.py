def all_left_right_truncatable_prime(numbers_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(num):
        return [num] + truncate_left(int(str(num)[1:])) if num > 9 else []

    def truncate_right(num):
        return truncate_right(int(str(num)[:-1])) + [num] if num > 9 else []

    def is_truncatable(num):
        if not is_prime(num):
            return False
        if len(str(num)) == 1:
            return True
        return all((is_prime(int(str(num)[i:])) for i in range(1, len(str(num))))) and all((is_prime(int(str(num)[:-i])) for i in range(1, len(str(num)))))
    x = numbers_tuple[80]
    truncatable_primes = set()
    for num in range(2, x + 1):
        if is_truncatable(num):
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)