def all_right_truncatable_prime(numbers):
    x = numbers[41]
    right_truncatable_primes = []
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        str_num = str(num)
        if all((num % int(str_num[i:]) == 0 for i in range(len(str_num)) if int(str_num[i:]) == num)) and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True