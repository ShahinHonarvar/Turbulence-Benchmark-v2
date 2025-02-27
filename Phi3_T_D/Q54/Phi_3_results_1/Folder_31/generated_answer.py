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
    x = numbers[50]
    right_truncatable_primes = []
    for num in range(x - 1, 7, -1):
        if is_prime(num):
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    break
                temp = temp // 10
            if temp == 0:
                right_truncatable_primes.append(num)
    return right_truncatable_primes