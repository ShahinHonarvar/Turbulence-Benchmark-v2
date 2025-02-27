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

def all_right_truncatable_prime(numbers):
    x = numbers[19]
    right_truncatables = []
    for num in range(2, x):
        if is_prime(num):
            digits = [int(digit) for digit in str(num)]
            while digits:
                if not is_prime(int(''.join(map(str, digits)))):
                    break
                digits.pop()
            else:
                right_truncatables.append(num)
    return sorted(right_truncatables)