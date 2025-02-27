def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    primes = [2, 3, 5, 7]
    left_right_truncatable = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i + 1])):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable_prime(num) and ('0' not in str(num)):
            primes.append(num)
            left_right_truncatable.append(num)
    return sorted(left_right_truncatable, reverse=True)