def all_left_truncatable_prime(t):
    x = t[71]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(11, x, 2):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((int(str_num[:i]) in primes for i in range(1, len(str_num) + 1))):
            result.append(num)
    return sorted(result, reverse=True)