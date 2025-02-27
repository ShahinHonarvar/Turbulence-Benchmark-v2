def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers[618]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(11, x + 1, 2):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((is_prime(int(str_num[:i])) and is_prime(int(str_num[i:])) for i in range(1, len(str_num)))):
            result.append(num)
    return sorted(result)