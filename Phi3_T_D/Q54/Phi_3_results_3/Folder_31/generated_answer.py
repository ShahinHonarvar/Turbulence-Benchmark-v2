def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers, index=50):
    try:
        x = numbers[index]
    except IndexError:
        return []
    result = [i for i in range(2, x) if right_truncatable_prime(i)]
    result.sort(reverse=True)
    return result