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

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    x = numbers[67] if len(numbers) > 67 else 0
    for num in range(x, 1, -1):
        str_num = str(num)
        if not all((digit != '0' for digit in str_num)) and is_prime(num):
            rotated = []
            left_truncated, right_truncated = (False, False)
            for i in range(len(str_num)):
                if is_prime(int(str_num[i:])):
                    left_truncated = True
                else:
                    break
            for i in range(len(str_num) - 1, 0, -1):
                if is_prime(int(str_num[:i])):
                    right_truncated = True
                else:
                    break
            if left_truncated and right_truncated:
                truncatable_primes.append(num)
    return truncatable_primes