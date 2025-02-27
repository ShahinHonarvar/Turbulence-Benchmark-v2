def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_all_digits_non_zero(n):
    return all((digit != '0' for digit in str(n)))

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[433]
    truncatable_primes = []
    for num in range(x, 1, -1):
        str_num = str(num)
        if len(str_num) > 1 and is_prime(num) and is_all_digits_non_zero(num):
            left_truncatable = all((is_prime(int(str_num[i:])) for i in range(len(str_num))))
            right_truncatable = all((is_prime(int(str_num[:i + 1])) for i in range(len(str_num) - 1, -1, -1)))
            if left_truncatable and right_truncatable:
                truncatable_primes.append(num)
    return truncatable_primes