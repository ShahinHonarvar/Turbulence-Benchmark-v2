def all_left_truncatable_prime(numbers):
    x = numbers[31]

    def is_left_truncatable_prime(num):
        if num < 10:
            return num in [2, 3, 5, 7]
        return num.isprime() and is_left_truncatable_prime(int(str(num)[1:]))
    return sorted(filter(is_left_truncatable_prime, range(1, x)), reverse=True)