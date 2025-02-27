def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    trunc_primes = []
    x = numbers[89] if len(numbers) > 89 else 0
    for number in range(x, 1, -1):
        str_num = str(number)
        is_truncatable = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i + 1])):
                is_truncatable = False
                break
        if is_truncatable:
            trunc_primes.append(number)
    return trunc_primes