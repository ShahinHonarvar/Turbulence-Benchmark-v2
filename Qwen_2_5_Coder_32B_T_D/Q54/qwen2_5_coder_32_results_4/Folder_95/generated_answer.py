def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[77]
    result = []
    for num in range(2, x):
        n = num
        while n > 0 and is_prime(n):
            n //= 10
        if n == 0:
            result.append(num)
    return sorted(result)