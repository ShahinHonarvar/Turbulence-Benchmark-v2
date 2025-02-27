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

def all_right_truncatable_primes(integers):
    x = integers[65]
    truncatable_primes = []

    def check_truncatable(number):
        if x < 10:
            return False
        if number % 10 == 0 or not is_prime(number):
            return False
        str_num = str(number)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[:len(str_num) - i - 1])):
                return False
        return True
    for number in range(7, x):
        if check_truncatable(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)