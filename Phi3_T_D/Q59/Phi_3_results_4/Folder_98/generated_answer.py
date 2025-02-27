def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[8]
    truncatables = []
    for p in range(x - 1, 7, -2):
        if not (p % 10 == 0 or (str(p)[:-1] and (not is_prime(int(str(p)[:-1]))))):
            while p > 0:
                if not is_prime(p):
                    break
                p //= 10
            else:
                truncatables.append(numbers[8] - p)
    return sorted(truncatables, reverse=True)