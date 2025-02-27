def all_left_right_truncatable_prime(numbers):
    result = []
    for number in numbers:
        if number > 0 and is_left_right_truncatable_prime(number):
            result.append(number)
    result.sort(reverse=True)
    return result

def is_left_right_truncatable_prime(number):
    number_str = str(number)
    if not number_str[0].isdigit() or not number_str[-1].isdigit():
        return False
    for i in range(1, len(number_str)):
        if not is_prime(int(number_str[i:])) or not is_prime(int(number_str[:len(number_str) - i])):
            return False
    return True

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True