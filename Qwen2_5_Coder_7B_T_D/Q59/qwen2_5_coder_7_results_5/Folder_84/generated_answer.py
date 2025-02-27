def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[630]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            if '0' not in str_num:
                all_trunc = True
                for i in range(len(str_num)):
                    if not is_prime(int(str_num[i:])):
                        all_trunc = False
                        break
                if all_trunc:
                    left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)