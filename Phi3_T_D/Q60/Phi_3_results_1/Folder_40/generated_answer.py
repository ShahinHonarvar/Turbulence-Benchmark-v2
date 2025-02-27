def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[10]
    truncatable_primes = []
    for number in range(x, 1, -1):
        str_num = str(number)
        if all((is_prime(int(str_num[i:])) and is_prime(int(str_num[:i + 1])) for i in range(len(str_num)))):
            truncatable_primes.append(number)
    return truncatable_primes