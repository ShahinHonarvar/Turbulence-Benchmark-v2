def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and '0' not in str(num):
            temp = num
            while temp > 0 and is_prime(temp):
                temp = int(str(temp)[1:-1]) if len(str(temp)) > 2 else temp
            if temp <= 0 or is_prime(temp):
                primes.append(num)
    return sorted(primes)