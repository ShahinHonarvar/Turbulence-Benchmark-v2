def all_left_truncatable_prime(numbers):
    x = numbers[43]

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

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if str_n[i] == '0' or not is_prime(int(str_n[i:])):
                return False
        return True
    primes = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)