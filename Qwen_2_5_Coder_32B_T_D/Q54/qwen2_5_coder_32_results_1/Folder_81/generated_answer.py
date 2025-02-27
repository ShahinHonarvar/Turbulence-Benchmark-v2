def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[98]
    right_trunc_primes = []
    for num in range(2, x):
        str_num = str(num)
        is_trunc_prime = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[:len(str_num) - i])):
                is_trunc_prime = False
                break
        if is_trunc_prime:
            right_trunc_primes.append(num)
    return sorted(right_trunc_primes)