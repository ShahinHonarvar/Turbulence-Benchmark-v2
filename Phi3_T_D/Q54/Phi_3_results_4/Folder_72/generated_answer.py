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

def all_right_truncatable_prime(numbers):
    x = numbers[31]
    right_truncatables = []
    for number in range(x - 1, 1, -1):
        if is_prime(number):
            str_number = str(number)
            while len(str_number) > 1 and is_prime(int(str_number)):
                if len(str_number) == 2:
                    right_truncatables.append(number)
                str_number = str_number[:-1]
    return sorted(right_truncatables, reverse=True)