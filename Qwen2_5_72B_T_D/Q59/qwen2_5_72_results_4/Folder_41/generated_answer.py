def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[46]
    primes = []
    for num in range(2, x):
        temp = num
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        if temp == 0 and '0' not in str(num):
            primes.append(num)
    return sorted(primes, reverse=True)