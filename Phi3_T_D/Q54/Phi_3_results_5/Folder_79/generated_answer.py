def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(number, prime_set):
        if number == 0:
            return True
        if not is_prime(number):
            return False
        return is_right_truncatable_prime(number // 10, prime_set)
    prime_set = set()
    for num in range(2, numbers[91]):
        if is_prime(num):
            if is_right_truncatable_prime(num, prime_set):
                prime_set.add(num)
    return sorted(list(prime_set))