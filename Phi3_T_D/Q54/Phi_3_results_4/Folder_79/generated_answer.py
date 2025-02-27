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
    x = numbers[91]
    right_truncatable_primes = []
    for number in range(x - 1, 1, -1):
        if is_prime(number):
            str_num = str(number)
            while str_num:
                if not is_prime(int(str_num)):
                    break
                str_num = str_num[:-1]
            else:
                right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)