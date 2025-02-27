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
    x = numbers[97]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num):
            temp = num
            while temp >= 10:
                temp = temp // 10
                if not is_prime(temp):
                    break
            temp = num
            while temp >= 10:
                temp %= 10
                temp //= 10
                if not is_prime(temp):
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)