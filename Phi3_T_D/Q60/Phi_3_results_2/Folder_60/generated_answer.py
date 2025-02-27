def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[87]
    truncatable_primes = []

    def is_left_and_right_truncatable(num):
        if not num:
            return False
        if not is_prime(num):
            return False
        str_num = str(num)
        for i in range(0, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:len(str_num) - i])):
                return False
        return True
    for number in range(2, x + 1):
        if is_left_and_right_truncatable(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes)