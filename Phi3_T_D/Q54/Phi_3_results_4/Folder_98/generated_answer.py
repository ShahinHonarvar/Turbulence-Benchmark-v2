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
    x = numbers[8]
    right_truncatable_primes = []
    for num in range(x - 1, 0, -1):
        if is_prime(num):
            digits = list(str(num))
            for i in range(len(digits)):
                temp_num = int(''.join(digits[:len(digits) - i]))
                if temp_num < 10 or not is_prime(temp_num):
                    break
            else:
                right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes