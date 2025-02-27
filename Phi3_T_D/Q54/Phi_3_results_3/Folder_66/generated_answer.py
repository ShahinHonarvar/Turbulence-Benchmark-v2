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
    rightmost = numbers[25]
    truncatable_primes = []
    for num in range(rightmost - 1, 1, -1):
        str_num = str(num)
        if not str_num.endswith('0') and is_prime(num):
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[:-i])):
                    break
            else:
                truncatable_primes.append(num)
    return truncatable_primes