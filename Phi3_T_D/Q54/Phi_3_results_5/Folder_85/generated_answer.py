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

def right_truncatable_prime(start, end):
    right_truncatable_primes = []
    for num in range(start, end, -2):
        if is_prime(num):
            temp = num
            while temp % 10 != 0:
                if is_prime(temp):
                    right_truncatable_primes.append(temp)
                temp //= 10
    return sorted(right_truncatable_primes)

def all_right_truncatable_prime(numbers, index):
    try:
        x = numbers[index]
        if x < 2:
            return []
        return right_truncatable_prime(2, x)
    except IndexError:
        return []