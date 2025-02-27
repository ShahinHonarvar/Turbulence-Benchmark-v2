def all_left_truncatable_prime(numbers):

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
    x = numbers[79]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        str_num = str(num)
        while len(str_num) > 0:
            if not is_prime(int(str_num)):
                break
            str_num = str_num[1:]
        else:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)