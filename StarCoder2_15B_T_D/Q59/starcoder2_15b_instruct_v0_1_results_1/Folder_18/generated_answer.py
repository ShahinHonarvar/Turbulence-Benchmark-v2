def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[429]
    result = []
    for i in range(1, x):
        if '0' in str(i):
            continue
        num = i
        while num < x:
            if not is_prime(num):
                break
            num = int(str(num)[1:])
        else:
            result.append(i)
    return sorted(result, reverse=True)