def all_right_truncatable_prime(data):
    x = data[11]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable(n, prime_set):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    result = []
    prime_set = set()
    for num in range(2, x, 2):
        if num in prime_set or is_prime(num):
            if is_right_truncatable(num, prime_set):
                result.append(num)
            prime_set.update(set(str(num)))
    return sorted(result)