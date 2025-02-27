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

def is_left_and_right_truncatable(prime, number_as_str):
    if len(number_as_str) <= 2:
        return True
    if not is_prime(int(number_as_str[1:])) or not is_prime(int(number_as_str[:-1])):
        return False
    return is_left_and_right_truncatable(prime, number_as_str[1:-1])

def all_left_right_truncatable_prime(numbers):
    x = numbers[33]
    left_right_truncatables = []
    for number in range(23, x + 1):
        if is_left_and_right_truncatable(number, str(number)):
            left_right_truncatables.append(number)
    return left_right_truncatables