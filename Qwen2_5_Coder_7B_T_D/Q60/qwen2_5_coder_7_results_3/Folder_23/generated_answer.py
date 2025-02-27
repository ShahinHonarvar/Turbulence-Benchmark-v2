def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    primes = []
    for num in range(2, x + 1):
        if all((int(digit) != 0 and is_prime(num) for digit in str(num))):
            if is_left_right_truncatable_prime(num):
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
        if not is_prime(int(str_num[:len(str_num) - i])):
            return False
    return True