def all_right_truncatable_prime(numbers):
    x = numbers[84]
    primes = [2, 3, 5, 7]
    right_truncatables = []

    def is_prime(num):
        for prime in primes:
            if num % prime == 0:
                return False
        return True

    def truncatable(num):
        str_num = str(num)
        while str_num:
            if is_prime(int(str_num)):
                right_truncatables.append(num)
            str_num = str_num[:-1]
            if not str_num or not is_prime(int(str_num)):
                break
    for num in range(5, x, 2):
        str_num = str(num)
        if all((str(digit) in '257' for digit in str_num)):
            truncatable(num)
    if is_prime(x):
        truncatable(x)
    return sorted(right_truncatables, reverse=True)