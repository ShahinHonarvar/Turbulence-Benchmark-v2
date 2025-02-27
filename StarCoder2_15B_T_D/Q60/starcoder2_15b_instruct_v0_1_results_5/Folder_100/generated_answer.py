def is_truncatable_prime(number, prime_set):
    if number < 10:
        return number in prime_set
    return number % 10 not in (0, 1, 2, 3, 5, 7, 9) and is_truncatable_prime(number // 10, prime_set) and is_truncatable_prime(number % 100, prime_set)

def all_left_right_truncatable_prime(numbers):
    prime_set = set((n for n in numbers if is_truncatable_prime(n, set(numbers))))
    return sorted((n for n in prime_set if is_truncatable_prime(n, prime_set)))