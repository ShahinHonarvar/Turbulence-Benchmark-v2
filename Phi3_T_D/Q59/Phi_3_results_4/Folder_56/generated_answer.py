def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[30]
    left_truncatable_primes = []
    for num in range(2, x):
        if not '0' in str(num):
            prime_flag = True
            temp_num = num
            while temp_num > 0:
                if not is_prime(temp_num):
                    prime_flag = False
                    break
                temp_num = int(str(temp_num)[1:])
            if prime_flag:
                left_truncatable_primes.append(num)
    return left_truncatable_primes