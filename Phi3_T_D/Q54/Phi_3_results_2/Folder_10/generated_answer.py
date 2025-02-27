def all_right_truncatable_prime(numbers):
    prime_numbers = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def all_right_digits_removed(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[38]
    for num in range(x, 1, -1):
        if all_right_digits_removed(num):
            prime_numbers.append(num)
    prime_numbers.sort(reverse=True)
    return prime_numbers