def all_left_truncatable_prime(input_tuple):
    x = input_tuple[0]
    left_truncatable_primes = []
    for num in range(2, x):
        is_left_truncatable = True
        temp = num
        while temp > 0:
            digit = temp % 10
            if digit == 0 or not is_prime(temp):
                is_left_truncatable = False
                break
            temp //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True