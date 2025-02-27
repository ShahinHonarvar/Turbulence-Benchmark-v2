def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, prime_digits):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if int(str_n[i:]) not in prime_digits or int(str_n[:-i]) not in prime_digits:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    prime_digits = {2}
    for num in range(3, x + 1, 2):
        if str(num)[-1] not in '0468':
            if is_prime(num):
                prime_digits.add(num)
    return [num for num in prime_digits if is_truncatable_prime(num, prime_digits)]