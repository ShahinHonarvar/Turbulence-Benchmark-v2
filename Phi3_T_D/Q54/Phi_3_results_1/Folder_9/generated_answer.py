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
    x = numbers[29]
    truncatables = []
    for number in range(x - 1, 1, -1):
        if is_prime(number):
            string_number = str(number)
            while len(string_number) > 1:
                string_number = string_number[:-1]
                if not is_prime(int(string_number)):
                    break
            else:
                truncatables.append(number)
    return truncatables