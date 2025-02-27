def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((int(str_num[:i]) in primes and int(str_num[i:]) in primes for i in range(1, len(str_num)))):
            primes.append(num)
    return sorted(primes)