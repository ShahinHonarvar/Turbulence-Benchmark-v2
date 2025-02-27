def all_left_right_truncatable_prime(numbers):

    def is_prime(n, prime_set):
        if n in prime_set:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        prime_set.add(n)
        return True

    def is_left_right_truncatable(n, prime_set):
        if not is_prime(n, prime_set):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:]), prime_set) or not is_prime(int(str_n[:-i or None]), prime_set):
                return False
        return True
    prime_set = set()
    x = numbers[26]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable(num, prime_set):
            result.append(num)
    return result