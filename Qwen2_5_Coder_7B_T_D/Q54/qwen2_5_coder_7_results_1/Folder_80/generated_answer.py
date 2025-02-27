def all_right_truncatable_prime(numbers):
    x = numbers[14]
    primes = []
    for num in range(2, x):
        if all((int(num) % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            str_num = str(num)
            is_right_truncatable = True
            for i in range(len(str_num)):
                if int(str_num[:len(str_num) - i]) % i == 0:
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)