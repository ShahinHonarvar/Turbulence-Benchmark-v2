def all_left_truncatable_prime(numbers):
    x = numbers[767]

    def is_left_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        return is_prime(num) and is_left_truncatable_prime(int(str(num)[1:]))
    result = []
    for i in range(x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True