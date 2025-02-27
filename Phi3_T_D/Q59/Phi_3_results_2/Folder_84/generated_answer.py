import math

def all_left_truncatable_prime(numbers):
    x = numbers[630]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def left_truncatable(num_str):
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True
    result = []
    for num in range(7, x, 2):
        if str(num)[0] == '2':
            continue
        num_str = str(num)
        if left_truncatable(num_str):
            result.append(num)
    return result