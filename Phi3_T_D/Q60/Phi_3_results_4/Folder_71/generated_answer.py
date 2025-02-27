def all_left_right_truncatable_prime(numbers):
    x = numbers[22]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if all((num % p != 0 for p in primes)):
            primes.append(num)
    truncatables = [p for p in primes if p <= x and all(is_truncatable(p))]
    return sorted(truncatables, reverse=True)

def is_truncatable(number):
    str_num = str(number)
    left = right = True
    while len(str_num) > 1:
        if not is_prime(int(str_num)):
            left = False
            break
        str_num = str_num[1:-1]
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            right = False
            break
    return left and right

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True