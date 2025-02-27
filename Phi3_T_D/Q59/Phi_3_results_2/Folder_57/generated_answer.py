def all_left_truncatable_prime(numbers):
    LIMIT = numbers[54]

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

    def is_left_truncatable(n):
        str_n = str(n)
        while len(str_n) > 1:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    result = []
    for num in range(2, LIMIT, 2):
        if num % 5 != 0 and is_left_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)