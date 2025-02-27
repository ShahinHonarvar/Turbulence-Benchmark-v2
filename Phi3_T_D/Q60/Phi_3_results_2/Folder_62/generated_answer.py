def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    truncatable_primes = []

    def is_truncatable_prime(num, from_left=True):
        str_num = str(num)
        for i in range(len(str_num)):
            if from_left:
                sub_num = int(str_num[i:])
            else:
                sub_num = int(str_num[:-i - 1])
            if not is_prime(sub_num):
                return False
        return True
    for number in range(23, x + 1):
        if is_prime(number) and is_truncatable_prime(number) and is_truncatable_prime(number, from_left=False):
            truncatable_primes.append(number)
    return sorted(truncatable_primes)