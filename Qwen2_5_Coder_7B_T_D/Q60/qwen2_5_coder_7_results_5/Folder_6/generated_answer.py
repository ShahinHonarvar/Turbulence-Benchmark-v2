def all_left_right_truncatable_prime(numbers):
    x = numbers[74]
    primes = [2, 3, 5, 7]
    result = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num) and '0' not in str(num) and is_left_right_truncatable(num):
            result.append(num)
    return sorted(result)