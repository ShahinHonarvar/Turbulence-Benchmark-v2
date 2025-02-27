def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[85]
    truncatable_primes = []

    def is_truncatable(num, primes):
        temp_num = str(num)
        while temp_num:
            if not is_prime(int(temp_num)):
                return False
            temp_num = temp_num[1:]
        return True
    for number in range(2, x):
        string_number = str(number)
        if string_number[0] == '0':
            continue
        if is_prime(number) and is_truncatable(number, primes):
            truncatable_primes.append(number)
    return truncatable_primes