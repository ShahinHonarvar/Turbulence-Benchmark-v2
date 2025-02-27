def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(len(str(i)) - 1):
            if not is_prime(int(str(i)[j:])) or not is_prime(int(str(i)[:-j - 1])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

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