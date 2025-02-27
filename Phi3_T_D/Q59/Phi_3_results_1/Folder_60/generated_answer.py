def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_truncatable_prime(n):
    return all([is_prime(int(n[i:])) for i in range(len(n))]) and is_prime(int(n))

def all_left_truncatable_prime(numbers):
    x = numbers[87]
    return sorted([num for num in range(2, x) if left_truncatable_prime(str(num))])