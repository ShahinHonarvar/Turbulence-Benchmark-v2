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

def all_left_right_truncatable_prime(numbers):
    x = numbers[37]
    result = []

    def is_truncatable(num):
        if is_prime(num):
            str_num = str(num)
            return all((is_prime(int(str_num[i:])) and is_prime(int(str_num[:-i])) for i in range(1, len(str_num))))
        return False
    for num in range(2, x + 1):
        if is_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)