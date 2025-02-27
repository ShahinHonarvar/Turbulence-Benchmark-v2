from sympy import primerange

def all_right_truncatable_prime(numbers):
    x = numbers[645]
    right_truncatable_primes = []
    for num in primerange(2, x):
        str_num = str(num)
        is_right_truncatable = True
        for i in range(len(str_num)):
            if int(str_num[i:]) not in primerange(2, num + 1):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)