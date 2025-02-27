def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[81]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            str_num = str(num)
            for i in range(len(str_num)):
                if not is_prime(int(str_num[i:])):
                    break
            else:
                left_truncatable_primes.append(num)
    return left_truncatable_primes