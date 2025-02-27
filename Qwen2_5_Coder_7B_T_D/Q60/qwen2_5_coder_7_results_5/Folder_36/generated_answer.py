def all_left_right_truncatable_prime(numbers):
    x = numbers[992]
    primes = [2, 3, 5, 7]
    result = []

    def is_prime(n):
        if n < 2 or (n % 2 == 0 and n > 2):
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    for num in range(2, x + 1):
        if all((digit != '0' for digit in str(num))) and is_prime(num) and is_left_right_truncatable(num):
            primes.append(num)
            if num <= x:
                result.append(num)
    return sorted(result)