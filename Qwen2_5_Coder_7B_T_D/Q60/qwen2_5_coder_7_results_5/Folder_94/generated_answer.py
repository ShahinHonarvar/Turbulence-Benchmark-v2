def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    primes = []
    for num in range(2, x + 1):
        if all((int(digit) != 0 for digit in str(num))) and is_prime(num):
            str_num = str(num)
            is_truncatable = True
            for i in range(len(str_num)):
                if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:len(str_num) - i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes)

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