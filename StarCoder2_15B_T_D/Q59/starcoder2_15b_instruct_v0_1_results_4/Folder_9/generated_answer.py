def all_left_truncatable_prime(numbers):
    return [num for num in numbers if is_left_truncatable_prime(num)]

def is_left_truncatable_prime(number):
    if not is_prime(number):
        return False
    digits = [int(digit) for digit in str(number)]
    if 0 in digits:
        return False
    for i in range(len(digits) - 1):
        truncated_number = int(''.join((str(digit) for digit in digits[i + 1:])))
        if not is_prime(truncated_number):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True