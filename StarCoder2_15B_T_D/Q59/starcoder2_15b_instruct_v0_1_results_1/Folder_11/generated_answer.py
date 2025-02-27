def all_left_truncatable_prime(numbers):
    assert isinstance(numbers, tuple)
    assert all((isinstance(num, int) and num > 0 for num in numbers))
    x = numbers[86]
    result = []
    for num in range(2, x):
        is_left_truncatable = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(num)
    return sorted(result)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True