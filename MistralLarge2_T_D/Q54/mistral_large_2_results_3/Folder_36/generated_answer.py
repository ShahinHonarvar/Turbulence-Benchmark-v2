def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[992]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = num
            while temp != 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                primes.append(num)
    return sorted(primes)