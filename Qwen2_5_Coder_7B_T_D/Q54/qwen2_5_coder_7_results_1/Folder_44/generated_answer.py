import math

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x):
        temp_num = num
        while temp_num > 0:
            if not is_prime(temp_num):
                break
            temp_num //= 10
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)