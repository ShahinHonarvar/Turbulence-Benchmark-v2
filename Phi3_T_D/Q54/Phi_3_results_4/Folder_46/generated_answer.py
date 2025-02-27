def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

def all_right_truncatable_prime(numbers):
    x = numbers[33]
    truncates = [str(p) for p in range(2, x) if is_prime(p)]
    right_truncatables = []
    for num in truncates:
        while num:
            if is_prime(int(num)):
                right_truncatables.append(int(num))
            num = num[:-1]
    return sorted(set(right_truncatables))