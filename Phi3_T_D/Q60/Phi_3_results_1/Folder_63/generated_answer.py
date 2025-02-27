def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    truncatable_primes = [2, 3, 5, 7]
    for number in range(11, 10 ** len(str(x))):
        if str(number).count('0') == 0 and is_prime(number):
            added = False
            str_num = str(number)
            can_truncate = True
            for i in range(1, len(str_num)):
                trunc_left = int(str_num[i:])
                trunc_right = int(str_num[:-i])
                if not is_prime(trunc_left) or not is_prime(trunc_right):
                    can_truncate = False
                    break
            if can_truncate:
                truncatable_primes.append(number)
    return sorted(list(filter(lambda n: n <= x, truncatable_primes)))