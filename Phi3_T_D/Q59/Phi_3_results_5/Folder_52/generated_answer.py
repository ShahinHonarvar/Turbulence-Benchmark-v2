def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[52]
    left_truncatable = []
    for n in range(2, x):
        if not '0' in str(n):
            if is_prime(n):
                truncatable = True
                num = str(n)
                while len(num) > 1 and is_prime(int(num)):
                    num = num[1:]
                    truncatable = truncatable and is_prime(int(num))
                if truncatable:
                    left_truncatable.append(n)
    return sorted(left_truncatable, reverse=True)