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

def all_left_truncatable_prime(numbers):
    x = numbers[38]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            str_num = str(num)
            if all((is_prime(int(str_num[i:])) for i in range(len(str_num)))):
                left_truncatable_primes.append(num)
    return left_truncatable_primes