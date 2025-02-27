def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    return all((is_prime(n) for n in [n] + [int(str(n)[:i]) for i in range(1, len(str(n)) + 1)]))

def all_right_truncatable_prime(numbers):
    x = numbers[81]
    return sorted([num for num in range(x - 1, 0, -1) if is_primal_priminess(num)], reverse=True)