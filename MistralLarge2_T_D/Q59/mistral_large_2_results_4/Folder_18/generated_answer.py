def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    while num_str:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[429]
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes