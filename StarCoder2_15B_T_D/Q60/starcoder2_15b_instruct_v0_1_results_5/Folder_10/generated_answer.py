def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(number):
        number_str = str(number)
        while len(number_str) >= 2:
            if not is_prime(int(number_str)):
                return False
            number_str = number_str[1:]
            number_str = number_str[:-1]
        return is_prime(int(number_str))
    return sorted([number for number in numbers if is_left_right_truncatable_prime(number)], reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True