def all_left_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]

    def is_prime(n):
        for prime in primes:
            if n % prime == 0:
                return False
        return True
    x = numbers[792]
    left_truncatable = []
    for number in range(11, x):
        str_num = str(number)
        if all((is_prime(int(str_num[i:])) and int(str_num[i]) != 0 for i in range(len(str_num)))):
            left_truncatable.append(number)
    return left_truncatable