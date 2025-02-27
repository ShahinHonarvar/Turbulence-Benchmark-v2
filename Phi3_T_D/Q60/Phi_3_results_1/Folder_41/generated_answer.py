def all_left_right_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n in primes:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_suftruncatable(n):
        n_str = str(n)
        if not is_prime(n):
            return False
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:-i])):
                return False
        return True
    x = numbers[46]
    result = [i for i in range(x, 1, -1) if is_suftruncatable(i)]
    return result