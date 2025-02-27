def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) != 1 or type(numbers[0]) is not int or numbers[0] < 10:
        raise ValueError('The input should be a tuple with one positive integer.')
    x = numbers[0]
    truncatable_primes = []

    def is_truncatable_prime(number):
        str_num = str(number)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                return False
        return True
    for num in range(x, 1, -1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)