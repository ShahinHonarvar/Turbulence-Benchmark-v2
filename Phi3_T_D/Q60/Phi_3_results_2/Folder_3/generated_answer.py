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
    x = numbers[100]
    if is_prime(x) and x > 11:
        truncatable_primes = []
        for i in range(11, x + 1):
            str_i = str(i)
            if is_prime(i):
                if all((is_prime(int(str_i[j:])) and is_prime(int(str_i[:len(str_i) - j])) for j in range(1, len(str_i)))):
                    truncatable_primes.append(i)
        return truncatable_primes
    else:
        return []