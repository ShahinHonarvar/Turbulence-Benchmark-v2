def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    right_truncatable_primes = []

    def is_right_truncatable_prime(number):
        truncatable = True
        temp_num = number
        while temp_num > 0:
            if not is_prime(temp_num):
                truncatable = False
                break
            temp_num = temp_num // 10
        return truncatable
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return right_truncatable_primes