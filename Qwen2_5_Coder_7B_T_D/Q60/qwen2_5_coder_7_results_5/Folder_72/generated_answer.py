def all_left_right_truncatable_prime(numbers):
    x = numbers[31]
    primes = []
    for num in range(2, x + 1):
        if all((int(digit) != 0 and is_prime(int(digit)) for digit in str(num))):
            left_truncatable = True
            right_truncatable = True
            temp = num
            while temp >= 10:
                if not is_prime(temp):
                    left_truncatable = False
                temp //= 10
            temp = num
            while temp >= 10:
                if not is_prime(temp):
                    right_truncatable = False
                temp = temp // 10 + temp % 10
            if left_truncatable and right_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True