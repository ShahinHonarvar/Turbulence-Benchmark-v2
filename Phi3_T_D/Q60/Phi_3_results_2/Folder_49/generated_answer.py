def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    k = numbers[14]
    left_right_primes = []

    def is_truncatable_prime(number):
        str_number = str(number)
        length = len(str_number)
        for i in range(length):
            if not is_prime(int(str_number[i:])):
                return False
            if not is_prime(int(str_number[:length - i])):
                return False
        return True
    for number in range(23, k + 1):
        if is_truncatable_prime(number):
            left_right_primes.append(number)
    return left_right_primes