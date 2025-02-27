def all_left_right_truncatable_prime(numbers):
    x = numbers[36]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        if n < 10:
            return []
        return [n] + truncate_left(int(str(n)[1:]))

    def truncate_right(n):
        if n < 10:
            return []
        return truncate_right(int(str(n)[:-1])) + [n]

    def is_truncatable(n):
        left = truncate_left(n)
        right = truncate_right(n)
        return set(left).issubset(prime_numbers) and set(right).issubset(prime_numbers)
    prime_numbers = [num for num in range(2, x + 1) if is_prime(num)]
    return sorted(list({n for n in prime_numbers if is_truncatable(n)}))