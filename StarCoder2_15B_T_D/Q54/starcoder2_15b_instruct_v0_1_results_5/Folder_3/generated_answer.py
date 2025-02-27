def is_prime(n: int) -> bool:
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

def all_right_truncatable_prime(args: tuple) -> list:
    x = args[0]
    if x < 100:
        return []
    result = []
    for i in range(100, x):
        num = i
        while num >= 10:
            if not is_prime(num):
                break
            num //= 10
        if num == 2 or num == 3:
            result.append(i)
    return sorted(result)