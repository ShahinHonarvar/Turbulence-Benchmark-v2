def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable(n, primes):
    if not is_prime(n):
        return False
    if str(n)[0] in {'0', '2', '4', '5', '6', '8'}:
        return False
    for i in range(len(n)):
        if not is_prime(int(n[i:])) or not is_prime(int(n[:i + 1])):
            return False
    return True

def all_left_and_right_truncatable_prime(numbers):
    x = numbers[88]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_and_right_truncatable(str(num), [2, 3, 5, 7]):
            truncatable_primes.append(num)
    return truncatable_primes