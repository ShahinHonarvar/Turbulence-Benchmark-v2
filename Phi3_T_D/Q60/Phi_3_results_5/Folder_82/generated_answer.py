def all_left_right_truncatable_prime(numbers):
    to_int = {str(i): i for i in range(10)}

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(to_int[str_n[:i]]) or not is_prime(to_int[str_n[i:]]):
                return False
        return True
    truncatable_primes = [n for n in range(23, numbers[69] + 1, 10) if is_truncatable(n)]
    return truncatable_primes[::-1]