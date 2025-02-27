def all_right_truncatable_prime(numbers):
    x = numbers[81]
    primes = set()
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            str_num = str(num)
            while str_num:
                if int(str_num) in primes:
                    break
                is_right_truncatable = True
                for j in range(len(str_num) - 1):
                    if int(str_num[:j + 1]) not in primes:
                        is_right_truncatable = False
                        break
                if is_right_truncatable:
                    primes.add(int(str_num))
                str_num = str_num[:-1]
    return sorted(primes, reverse=True)