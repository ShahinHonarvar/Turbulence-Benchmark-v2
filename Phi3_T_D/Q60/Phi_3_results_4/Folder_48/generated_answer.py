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

def is_left_right_truncatable(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])) or (i == 0 and (not str_n[i].isdigit())) or (i == len(str_n) - 1 and (not str_n[i].isdigit())):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[835]
    result = []
    for number in range(2, x + 1):
        if is_left_right_truncatable(number):
            result.append(number)
    return result