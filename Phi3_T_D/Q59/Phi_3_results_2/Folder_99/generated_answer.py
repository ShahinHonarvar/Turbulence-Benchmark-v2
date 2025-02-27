def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[758]
    truncatables = []

    def is_left_truncatable(num, x):
        if not is_prime(num):
            return False
        str_num = str(num)
        return all((is_prime(int(str_num[i:])) for i in range(len(str_num))))
    for number in range(2, x):
        if is_left_truncatable(number, x):
            truncatables.append(number)
    return sorted(truncatables)