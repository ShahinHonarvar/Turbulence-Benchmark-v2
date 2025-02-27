def all_left_right_truncatable_prime(numbers):
    x = numbers[52]
    primes = [2, 3, 5, 7]
    result = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(3, x + 1, 2):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        is_truncatable = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_truncatable = False
                break
            if not is_prime(int(str_num[:len(str_num) - i])):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return sorted(result, reverse=True)