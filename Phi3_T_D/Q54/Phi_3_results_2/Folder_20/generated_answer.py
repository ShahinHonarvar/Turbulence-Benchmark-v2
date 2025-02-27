def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    if not 2 <= numbers[100] <= 10 ** 6:
        return []
    tens, ones = divmod(numbers[100], 10)
    result = []
    for candidate in range(ones, tens, -1):
        if is_prime(candidate) and all((is_prime(candidate % 10 ** i) for i in range(len(str(candidate)))[::-1])):
            result.append(candidate)
    return result