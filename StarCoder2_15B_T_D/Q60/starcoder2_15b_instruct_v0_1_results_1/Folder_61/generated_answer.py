def is_trunctable_prime(number):
    number_str = str(number)
    for i in range(len(number_str)):
        truncated_number = int(number_str[i:])
        if not is_prime(truncated_number):
            return False
        truncated_number = int(number_str[:len(number_str) - i])
        if not is_prime(truncated_number):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for number in range(10, x + 1):
        if is_trunctable_prime(number):
            result.append(number)
    result.sort(reverse=True)
    return result